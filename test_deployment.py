#!/usr/bin/env python3
"""
Backend Deployment Test Script
Tests if your backend is properly deployed and responding.
"""

import requests
import json
import sys
from datetime import datetime

def test_endpoint(url, name):
    """Test a specific endpoint and return results"""
    try:
        print(f"🔍 Testing {name}...")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ {name}: SUCCESS (Status: {response.status_code})")
            try:
                data = response.json()
                print(f"   Response: {json.dumps(data, indent=2)}")
            except:
                print(f"   Response: {response.text[:200]}...")
            return True
        else:
            print(f"❌ {name}: FAILED (Status: {response.status_code})")
            print(f"   Response: {response.text[:200]}...")
            return False
            
    except requests.exceptions.Timeout:
        print(f"⏰ {name}: TIMEOUT (Service not responding)")
        return False
    except requests.exceptions.ConnectionError:
        print(f"🔌 {name}: CONNECTION ERROR (Service not reachable)")
        return False
    except Exception as e:
        print(f"💥 {name}: ERROR - {str(e)}")
        return False

def main():
    print("🚀 BACKEND DEPLOYMENT TEST")
    print("=" * 50)
    
    # Get app name from user
    app_name = input("Enter your Render app name (e.g., autogen-backend): ").strip()
    
    if not app_name:
        print("❌ Please provide an app name!")
        return
    
    base_url = f"https://{app_name}.onrender.com"
    
    print(f"\n🎯 Testing backend at: {base_url}")
    print("=" * 50)
    
    # Test endpoints
    endpoints = [
        (f"{base_url}/health", "Health Check"),
        (f"{base_url}/api/health", "API Health"),
        (f"{base_url}/", "Root Endpoint")
    ]
    
    results = []
    for url, name in endpoints:
        result = test_endpoint(url, name)
        results.append(result)
        print()
    
    # Summary
    print("=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    successful = sum(results)
    total = len(results)
    
    if successful == total:
        print(f"🎉 ALL TESTS PASSED! ({successful}/{total})")
        print("✅ Your backend is properly deployed and working!")
    elif successful > 0:
        print(f"⚠️  PARTIAL SUCCESS ({successful}/{total} tests passed)")
        print("🔧 Some endpoints may need attention")
    else:
        print(f"❌ ALL TESTS FAILED ({successful}/{total})")
        print("🚨 Your backend may not be deployed or has issues")
    
    print(f"\n📅 Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Additional checks
    print("\n🔍 ADDITIONAL CHECKS:")
    print("1. Check Render Dashboard: https://dashboard.render.com")
    print("2. Verify service status is 'Live'")
    print("3. Check logs for any errors")
    print("4. Ensure environment variables are set")

if __name__ == "__main__":
    main()
