// Configuration for different environments
const config = {
  // Development environment
  development: {
    apiBaseUrl: '', // Uses relative URLs with Vite proxy
  },
  // Production environment (GitHub Pages)
  production: {
    apiBaseUrl: 'https://autogen-backend-32x7.onrender.com', // Your Render backend URL
  }
};

// Determine current environment
const isDevelopment = import.meta.env.DEV;
const currentConfig = config[isDevelopment ? 'development' : 'production'];

export const API_BASE_URL = currentConfig.apiBaseUrl;

// Helper function to build API URLs
export const buildApiUrl = (endpoint) => {
  return `${API_BASE_URL}${endpoint}`;
};
