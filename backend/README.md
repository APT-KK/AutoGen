# AutoGen Backend

This directory contains all backend-related functionality for the AutoGen project.

## Structure

```
backend/
├── __init__.py              # Package initialization
├── backend.py               # Main backend logic
├── model.py                 # AI model integration
├── githubHandler.py         # GitHub API integration
├── projectCreator.py        # Project generation logic
├── config.py                # Configuration management
├── utils.py                 # Utility functions
├── wsgi.py                  # WSGI entry point
├── requirements.txt         # Development dependencies
├── requirements-prod.txt    # Production dependencies
├── Dockerfile               # Container configuration
├── docker-compose.yml       # Multi-container setup
├── env.example              # Environment variables template
└── README.md               # This file
```

## Setup

### Development Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp env.example .env
   # Edit .env with your actual values
   ```

3. **Run the development server:**
   ```bash
   python wsgi.py
   ```

### Production Setup

#### Option 1: Docker (Recommended)

1. **Build and run with Docker Compose:**
   ```bash
   docker-compose up -d
   ```

2. **For production with nginx:**
   ```bash
   docker-compose --profile production up -d
   ```

#### Option 2: Direct Deployment

1. **Install production dependencies:**
   ```bash
   pip install -r requirements-prod.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp env.example .env
   # Edit .env with production values
   ```

3. **Run with Gunicorn:**
   ```bash
   gunicorn --bind 0.0.0.0:5000 --workers 4 wsgi:app
   ```

## Environment Variables

Required environment variables:

- `FLASK_SECRET_KEY`: Secret key for Flask sessions
- `GOOGLE_API_KEY`: Google Generative AI API key
- `GITHUB_TOKEN`: GitHub personal access token
- `GITHUB_USERNAME`: GitHub username for repository creation

Optional environment variables:

- `FIGMA_TOKEN`: Figma API token for design imports
- `FLASK_DEBUG`: Set to "True" for development
- `LOG_LEVEL`: Logging level (INFO, DEBUG, WARNING, ERROR)
- `PORT`: Server port (default: 5000)

## API Endpoints

The backend provides the following endpoints:

- `POST /generate`: Generate a new project
- `GET /projects/<project_id>`: Get project files
- `GET /health`: Health check endpoint

## Deployment

### Docker Deployment

1. **Build the image:**
   ```bash
   docker build -t autogen-backend .
   ```

2. **Run the container:**
   ```bash
   docker run -p 5000:5000 --env-file .env autogen-backend
   ```

### Cloud Deployment

#### Heroku
```bash
heroku create your-app-name
heroku config:set FLASK_ENV=production
git push heroku main
```

#### AWS ECS
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin your-account.dkr.ecr.us-east-1.amazonaws.com
docker tag autogen-backend:latest your-account.dkr.ecr.us-east-1.amazonaws.com/autogen-backend:latest
docker push your-account.dkr.ecr.us-east-1.amazonaws.com/autogen-backend:latest
```

## Monitoring

The application includes health checks and logging:

- Health check endpoint: `GET /health`
- Logs are written to stdout/stderr for container environments
- Structured logging with configurable levels

## Security

- Path traversal protection in file operations
- Environment variable configuration
- Non-root user in Docker containers
- Input validation and sanitization

## Troubleshooting

### Common Issues

1. **Import errors:** Ensure you're running from the correct directory
2. **API key errors:** Verify all required environment variables are set
3. **Permission errors:** Check file permissions for projects and uploads directories

### Logs

Check application logs for detailed error information:

```bash
# Docker
docker logs <container_name>

# Direct deployment
tail -f /var/log/autogen-backend.log
```
