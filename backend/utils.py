# Utility functions for backend operations
import os
import base64
import logging
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlparse, parse_qs
import requests

logger = logging.getLogger(__name__)

def safe_join(base: str, rel: str) -> str:
    """Safely join paths to prevent directory traversal attacks"""
    base_real = os.path.realpath(base)
    target = os.path.realpath(os.path.join(base_real, rel))
    if target == base_real or target.startswith(base_real + os.sep):
        return target
    raise PermissionError("Path traversal detected")

def extract_figma_key_and_node(figma_url: str) -> Tuple[Optional[str], Optional[str]]:
    """Extract Figma file key and node ID from URL"""
    try:
        u = urlparse(figma_url)
        parts = [p for p in u.path.split("/") if p]
        key = None
        if len(parts) >= 2 and parts[0] in ("file", "design"):
            key = parts[1]
        q = parse_qs(u.query)
        node = q.get("node-id", [None])[0]
        return key, node
    except Exception as e:
        logger.error(f"Error extracting Figma key and node: {e}")
        return None, None

def download_figma_image(figma_url: str, token: str, uploads_dir: Path) -> Optional[str]:
    """Download image from Figma API"""
    key, node = extract_figma_key_and_node(figma_url)
    if not key or not token:
        return None

    try:
        headers = {"X-FIGMA-TOKEN": token}
        if not node:
            meta = requests.get(f"https://api.figma.com/v1/files/{key}", headers=headers, timeout=30)
            meta.raise_for_status()
            data = meta.json()
            node = data.get("document", {}).get("children", [{}])[0].get("id")
            if not node:
                return None

        imgs = requests.get(
            f"https://api.figma.com/v1/images/{key}",
            headers=headers,
            params={"ids": node, "format": "png", "scale": 2},
            timeout=30,
        )
        imgs.raise_for_status()
        img_url = imgs.json().get("images", {}).get(node)
        if not img_url:
            return None

        img_resp = requests.get(img_url, timeout=60)
        img_resp.raise_for_status()
        uploads_dir.mkdir(parents=True, exist_ok=True)
        out_path = uploads_dir / f"figma_{key}_{node.replace(':','-')}.png"
        out_path.write_bytes(img_resp.content)
        return str(out_path)
    except Exception as e:
        logger.error(f"Error downloading Figma image: {e}")
        return None

def save_canvas_png(data_url: str, dest_dir: Path) -> Optional[str]:
    """Save canvas PNG from data URL"""
    if not data_url or not data_url.startswith("data:image/"):
        return None
    try:
        _, b64 = data_url.split(",", 1)
        raw = base64.b64decode(b64)
        dest_dir.mkdir(parents=True, exist_ok=True)
        out = dest_dir / "canvas_wireframe.png"
        out.write_bytes(raw)
        return str(out)
    except Exception as e:
        logger.error(f"Error saving canvas PNG: {e}")
        return None

def save_uploaded_file(file_storage, dest_dir: Path) -> Optional[str]:
    """Save uploaded file to destination directory"""
    if not file_storage or not getattr(file_storage, "filename", ""):
        return None
    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
        out = dest_dir / file_storage.filename
        file_storage.save(out)
        return str(out)
    except Exception as e:
        logger.error(f"Error saving uploaded file: {e}")
        return None

def validate_file_extension(filename: str, allowed_extensions: set) -> bool:
    """Validate file extension"""
    if not filename:
        return False
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

def generate_project_id() -> str:
    """Generate unique project ID"""
    import uuid
    return f"site-{uuid.uuid4().hex[:8]}"

def cleanup_old_files(directory: Path, max_age_hours: int = 24) -> None:
    """Clean up old files from directory"""
    import time
    current_time = time.time()
    max_age_seconds = max_age_hours * 3600
    
    try:
        for file_path in directory.iterdir():
            if file_path.is_file():
                file_age = current_time - file_path.stat().st_mtime
                if file_age > max_age_seconds:
                    file_path.unlink()
                    logger.info(f"Cleaned up old file: {file_path}")
    except Exception as e:
        logger.error(f"Error cleaning up old files: {e}")
