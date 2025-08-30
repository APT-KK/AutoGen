# Configuration file for backend settings
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Projects directory
PROJECTS_DIR = BASE_DIR / "projects"

# Flask configuration
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "False").lower() == "true"

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Figma configuration
FIGMA_TOKEN = os.getenv("FIGMA_TOKEN")

# File upload settings
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
UPLOAD_FOLDER = BASE_DIR / "uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg'}

# GitHub settings
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_REPO_PREFIX = os.getenv("GITHUB_REPO_PREFIX", "autogen-site")

# Model settings
DEFAULT_MODEL = "gemini-2.0-flash"
MAX_TOKENS = 8192

# Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Ensure directories exist
PROJECTS_DIR.mkdir(exist_ok=True)
UPLOAD_FOLDER.mkdir(exist_ok=True)
