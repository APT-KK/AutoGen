# 🚀 Quick Deploy Guide for AutoGen Backend

## ✅ Current Setup

Your project is now properly configured for Render deployment with:
- `render.yaml` in the root directory
- All backend files in the `backend/` directory
- Proper build and start commands

## 🎯 Deployment Steps

### Option 1: Using render.yaml (Recommended)

1. **Push your code to GitHub** (if not already done)
2. **Go to Render Dashboard**: https://dashboard.render.com
3. **Click "New +" → "Blueprint"**
4. **Connect your GitHub repository**
5. **Render will automatically detect the render.yaml file**
6. **Click "Apply" to deploy**

### Option 2: Manual Setup

1. **Go to Render Dashboard**: https://dashboard.render.com
2. **Click "New +" → "Web Service"**
3. **Connect your GitHub repository**
4. **Configure manually**:
   - **Name**: `autogen-backend`
   - **Root Directory**: Leave empty (uses root)
   - **Runtime**: `Python 3`
   - **Build Command**: `cd backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && gunicorn --bind 0.0.0.0:$PORT wsgi:app`

## 🔧 Environment Variables

Set these in Render dashboard → Environment tab:

```
FLASK_ENV=production
FLASK_SECRET_KEY=505d8221bfd422066640975899b69d5e62addcb897c7cbca84d0dcfe18055cf1
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY_HERE
GITHUB_TOKEN=YOUR_GITHUB_TOKEN_HERE
GITHUB_USERNAME=YOUR_GITHUB_USERNAME
FIGMA_TOKEN=YOUR_FIGMA_TOKEN_HERE
LOG_LEVEL=INFO
PYTHON_VERSION=3.11.0
```

## ✅ Verification

After deployment, test:
- **Health Check**: `https://your-app-name.onrender.com/health`
- **API Health**: `https://your-app-name.onrender.com/api/health`

## 🔍 Troubleshooting

If you get "Service Root Directory missing" error:
1. Ensure `render.yaml` is in the root directory (✅ Done)
2. Ensure all backend files are in `backend/` directory (✅ Done)
3. The build command should be: `cd backend && pip install -r requirements.txt` (✅ Done)

## 📁 File Structure

```
AutoGen/
├── render.yaml              # Render configuration (root level)
├── app.py                   # Main Flask app
├── backend/                 # Backend package
│   ├── __init__.py
│   ├── backend.py
│   ├── model.py
│   ├── githubHandler.py
│   ├── projectCreator.py
│   ├── config.py
│   ├── utils.py
│   ├── wsgi.py              # WSGI entry point
│   ├── requirements.txt     # Dependencies
│   ├── Procfile            # Process file
│   └── runtime.txt         # Python version
├── projects/               # Generated projects
└── uploads/                # File uploads
```

Your backend should now deploy successfully! 🎉
