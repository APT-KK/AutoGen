#!/usr/bin/env python3
"""
Key Generator for AutoGen Backend Deployment
Generates secure keys for Flask and provides instructions for other API keys.
"""

import secrets
import string
import random

def generate_flask_secret_key():
    """Generate a secure Flask secret key"""
    return secrets.token_hex(32)

def generate_random_string(length=32):
    """Generate a random string for additional security"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("🔐 AUTO-GEN BACKEND KEY GENERATOR")
    print("=" * 50)
    
    # Generate Flask Secret Key
    flask_key = generate_flask_secret_key()
    print(f"\n✅ FLASK_SECRET_KEY:")
    print(f"   {flask_key}")
    
    # Generate alternative Flask key
    flask_key_alt = generate_random_string(64)
    print(f"\n✅ ALTERNATIVE FLASK_SECRET_KEY:")
    print(f"   {flask_key_alt}")
    
    print("\n" + "=" * 50)
    print("🔑 API KEYS YOU NEED TO GENERATE MANUALLY:")
    print("=" * 50)
    
    print("\n1️⃣ GOOGLE_API_KEY:")
    print("   • Go to: https://makersuite.google.com/app/apikey")
    print("   • Sign in with your Google account")
    print("   • Click 'Create API Key'")
    print("   • Copy the generated key (starts with 'AIzaSyC...')")
    
    print("\n2️⃣ GITHUB_TOKEN:")
    print("   • Go to: https://github.com/settings/tokens")
    print("   • Click 'Generate new token (classic)'")
    print("   • Give it a name: 'AutoGen Backend'")
    print("   • Select scopes: 'repo' (full control of private repositories)")
    print("   • Click 'Generate token'")
    print("   • Copy the token (starts with 'ghp_...')")
    
    print("\n3️⃣ FIGMA_TOKEN:")
    print("   • Go to: https://www.figma.com/developers/api#access-tokens")
    print("   • Log into Figma")
    print("   • Go to Settings → Account → Personal access tokens")
    print("   • Click 'Create new token'")
    print("   • Give it a name: 'AutoGen Integration'")
    print("   • Copy the generated token")
    
    print("\n" + "=" * 50)
    print("📋 ENVIRONMENT VARIABLES FOR RENDER:")
    print("=" * 50)
    
    print(f"\nFLASK_ENV=production")
    print(f"FLASK_SECRET_KEY={flask_key}")
    print(f"GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY_HERE")
    print(f"GITHUB_TOKEN=YOUR_GITHUB_TOKEN_HERE")
    print(f"GITHUB_USERNAME=YOUR_GITHUB_USERNAME")
    print(f"FIGMA_TOKEN=YOUR_FIGMA_TOKEN_HERE")
    print(f"LOG_LEVEL=INFO")
    
    print("\n" + "=" * 50)
    print("⚠️  IMPORTANT SECURITY NOTES:")
    print("=" * 50)
    print("• Never commit these keys to your repository")
    print("• Store them securely in Render's environment variables")
    print("• Rotate keys regularly for security")
    print("• Keep your API keys private and don't share them")

if __name__ == "__main__":
    main()
