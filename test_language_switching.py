#!/usr/bin/env python
"""
Test script to verify language switching functionality
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dorsamehrkish.settings')
django.setup()

from django.test import Client
from django.urls import reverse
from django.utils.translation import activate, gettext as _

def test_language_switching():
    """Test the language switching functionality"""
    client = Client()
    
    print("=== Testing Language Switching ===")
    
    # Test 1: Default language (English)
    print("\n1. Testing default language (English):")
    response = client.get('/')
    print(f"   Status: {response.status_code}")
    print(f"   Content contains 'Home': {'Home' in str(response.content)}")
    
    # Test 2: Switch to Persian
    print("\n2. Testing Persian language switch:")
    response = client.post('/i18n/setlang/', {'language': 'fa', 'next': '/'}, follow=True)
    print(f"   Status: {response.status_code}")
    print(f"   Content contains 'خانه': {'خانه' in str(response.content)}")
    
    # Test 3: Check if language cookie is set
    print("\n3. Testing language cookie:")
    if 'django_language' in response.cookies:
        print(f"   Language cookie set to: {response.cookies['django_language'].value}")
    else:
        print("   No language cookie found")
    
    # Test 4: Test Persian URL
    print("\n4. Testing Persian URL:")
    response = client.get('/fa/')
    print(f"   Status: {response.status_code}")
    print(f"   Content contains 'خانه': {'خانه' in str(response.content)}")
    
    # Test 5: Test English URL
    print("\n5. Testing English URL:")
    response = client.get('/en/')
    print(f"   Status: {response.status_code}")
    print(f"   Content contains 'Home': {'Home' in str(response.content)}")
    
    # Test 6: Switch back to English
    print("\n6. Testing switch back to English:")
    response = client.post('/i18n/setlang/', {'language': 'en', 'next': '/'}, follow=True)
    print(f"   Status: {response.status_code}")
    print(f"   Content contains 'Home': {'Home' in str(response.content)}")
    
    print("\n=== Language Switching Test Complete ===")

def test_translations():
    """Test individual translations"""
    print("\n=== Testing Individual Translations ===")
    
    # Test English
    activate('en')
    print(f"English 'Home': {_('Home')}")
    print(f"English 'About': {_('About')}")
    print(f"English 'Contact': {_('Contact')}")
    
    # Test Persian
    activate('fa')
    print(f"Persian 'Home': {_('Home')}")
    print(f"Persian 'About': {_('About')}")
    print(f"Persian 'Contact': {_('Contact')}")
    
    print("=== Translation Test Complete ===")

if __name__ == '__main__':
    test_language_switching()
    test_translations() 