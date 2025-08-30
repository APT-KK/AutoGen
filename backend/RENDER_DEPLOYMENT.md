# Deploying AutoGen Backend to Render

This guide will help you deploy your AutoGen backend to Render's free tier.

## Prerequisites

1. **GitHub Repository**: Your code should be in a GitHub repository
2. **Render Account**: Sign up at [render.com](https://render.com)
3. **API Keys**: You'll need your API keys ready (Google, GitHub, etc.)

## Step-by-Step Deployment

### 1. Prepare Your Repository

Ensure your repository structure looks like this:
```
AutoGen/
├── app.py                 # Main Flask app
├── backend/               # Backend package
│   ├── __init__.py
│   ├── backend.py
│   ├── model.py
│   ├── githubHandler.py
│   ├── projectCreator.py
│   ├── config.py
│   ├── utils.py
│   ├── wsgi.py            # WSGI entry point
│   ├── requirements.txt   # Dependencies
│   ├── Procfile           # Process file
│   ├── runtime.txt        # Python version
│   └── render.yaml        # Render configuration
├── projects/              # Generated projects
└── uploads/               # File uploads
```

### 2. Deploy to Render

#### Option A: Using Render Dashboard (Recommended)

1. **Go to Render Dashboard**
   - Visit [dashboard.render.com](https://dashboard.render.com)
   - Click "New +" → "Web Service"

2. **Connect Your Repository**
   - Connect your GitHub account
   - Select your AutoGen repository
   - Choose the repository

3. **Configure the Service**
   - **Name**: `autogen-backend` (or your preferred name)
   - **Root Directory**: `backend` (important!)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT wsgi:app`

4. **Set Environment Variables**
   Click "Environment" tab and add:
   ```
   FLASK_ENV=production
   FLASK_SECRET_KEY=your-secret-key-here
   GOOGLE_API_KEY=your-google-api-key
   GITHUB_TOKEN=your-github-token
   GITHUB_USERNAME=your-github-username
   FIGMA_TOKEN=your-figma-token (optional)
   LOG_LEVEL=INFO
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app

#### Option B: Using render.yaml (Infrastructure as Code)

1. **Push your code** to GitHub with the `render.yaml` file
2. **Go to Render Dashboard**
3. **Click "New +" → "Blueprint"**
4. **Connect your repository**
5. **Render will automatically detect and use the render.yaml configuration**

### 3. Post-Deployment Configuration

#### Set Up Environment Variables

In your Render dashboard, go to your service → Environment tab:

**Required Variables:**
- `FLASK_SECRET_KEY`: Generate a secure random string
- `GOOGLE_API_KEY`: Your Google Generative AI API key
- `GITHUB_TOKEN`: Your GitHub personal access token
- `GITHUB_USERNAME`: Your GitHub username

**Optional Variables:**
- `FIGMA_TOKEN`: Your Figma API token
- `LOG_LEVEL`: Set to INFO, DEBUG, WARNING, or ERROR

#### Configure Auto-Deploy

- Enable "Auto-Deploy" in your service settings
- Render will automatically redeploy when you push to your main branch

### 4. Testing Your Deployment

1. **Health Check**: Visit `https://your-app-name.onrender.com/health`
2. **API Test**: Test your main endpoints
3. **Monitor Logs**: Check the logs in Render dashboard

### 5. Custom Domain (Optional)

1. Go to your service settings
2. Click "Custom Domains"
3. Add your domain and configure DNS

## Troubleshooting

### Common Issues

1. **Build Failures**
   - Check that `requirements.txt` is in the `backend/` directory
   - Ensure all dependencies are listed
   - Check Python version compatibility

2. **Import Errors**
   - Verify `wsgi.py` is correctly importing from parent directory
   - Check that all backend modules are in the `backend/` package

3. **Environment Variables**
   - Ensure all required API keys are set
   - Check variable names match your code

4. **Port Issues**
   - Render automatically sets the `$PORT` environment variable
   - Your app must bind to `0.0.0.0:$PORT`

### Logs and Debugging

- **View Logs**: Go to your service → Logs tab
- **Real-time Logs**: Use the "Live" button for real-time monitoring
- **Build Logs**: Check build logs for dependency issues

## Performance Considerations

### Free Tier Limitations
- **Sleep after inactivity**: Your app will sleep after 15 minutes of inactivity
- **Cold starts**: First request after sleep may be slow
- **Bandwidth**: Limited bandwidth on free tier

### Optimization Tips
1. **Keep dependencies minimal**: Only include necessary packages
2. **Use environment variables**: Don't hardcode secrets
3. **Monitor usage**: Check your service metrics regularly

## Security Best Practices

1. **Environment Variables**: Never commit API keys to your repository
2. **HTTPS**: Render provides automatic HTTPS
3. **Secrets Management**: Use Render's environment variable encryption
4. **Input Validation**: Ensure your app validates all inputs

## Monitoring and Maintenance

1. **Health Checks**: Your app includes a `/health` endpoint
2. **Logs**: Monitor logs for errors and performance issues
3. **Updates**: Keep dependencies updated regularly
4. **Backups**: Consider backing up your generated projects

## Support

- **Render Documentation**: [docs.render.com](https://docs.render.com)
- **Render Community**: [community.render.com](https://community.render.com)
- **GitHub Issues**: For code-specific issues

## Example Deployment URL

Once deployed, your app will be available at:
```
https://your-app-name.onrender.com
```

Your API endpoints will be:
- Health check: `https://your-app-name.onrender.com/health`
- Generate: `https://your-app-name.onrender.com/api/generate`
- Download: `https://your-app-name.onrender.com/api/download`
