# Backend package for AutoGen
# This package contains all backend-related functionality

from .backend import create_and_deploy_project
from .model import get_data_from_agent
from .githubHandler import deploy_to_github, enable_github_pages
from .projectCreator import create_project_structure
from .config import *
from .utils import *

__all__ = [
    'create_and_deploy_project',
    'get_data_from_agent', 
    'deploy_to_github',
    'enable_github_pages',
    'create_project_structure',
    # Config exports
    'BASE_DIR',
    'PROJECTS_DIR',
    'FLASK_SECRET_KEY',
    'FLASK_DEBUG',
    'GOOGLE_API_KEY',
    'GITHUB_TOKEN',
    'FIGMA_TOKEN',
    'MAX_CONTENT_LENGTH',
    'UPLOAD_FOLDER',
    'ALLOWED_EXTENSIONS',
    'GITHUB_USERNAME',
    'GITHUB_REPO_PREFIX',
    'DEFAULT_MODEL',
    'MAX_TOKENS',
    'LOG_LEVEL',
    'LOG_FORMAT',
    # Utils exports
    'safe_join',
    'extract_figma_key_and_node',
    'download_figma_image',
    'save_canvas_png',
    'save_uploaded_file',
    'validate_file_extension',
    'generate_project_id',
    'cleanup_old_files'
]
