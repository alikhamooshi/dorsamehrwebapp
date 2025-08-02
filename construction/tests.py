from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from django.utils import translation


class LanguageSwitchingTest(TestCase):
    """Test cases for language switching functionality"""
    
    def setUp(self):
        self.client = Client()
    
    def test_set_language_view(self):
        """Test that the set_language view works correctly"""
        # Test switching to Persian
        response = self.client.post(reverse('construction:set_language'), {
            'language': 'fa'
        }, HTTP_REFERER='http://testserver/')
        
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(response.cookies[settings.LANGUAGE_COOKIE_NAME].value, 'fa')
        
        # Test switching to English
        response = self.client.post(reverse('construction:set_language'), {
            'language': 'en'
        }, HTTP_REFERER='http://testserver/')
        
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(response.cookies[settings.LANGUAGE_COOKIE_NAME].value, 'en')
    
    def test_invalid_language(self):
        """Test that invalid language codes are handled properly"""
        response = self.client.post(reverse('construction:set_language'), {
            'language': 'invalid'
        })
        
        self.assertEqual(response.status_code, 302)  # Should redirect to home
    
    def test_language_context_processor(self):
        """Test that language context processor provides correct variables"""
        # Set language to Persian
        translation.activate('fa')
        
        response = self.client.get(reverse('construction:home'))
        self.assertEqual(response.status_code, 200)
        
        # Check that context variables are available
        self.assertIn('current_language', response.context)
        self.assertIn('available_languages', response.context)
        self.assertIn('is_rtl', response.context)
        
        self.assertEqual(response.context['current_language'], 'fa')
        self.assertTrue(response.context['is_rtl'])
        
        # Set language to English
        translation.activate('en')
        
        response = self.client.get(reverse('construction:home'))
        self.assertEqual(response.context['current_language'], 'en')
        self.assertFalse(response.context['is_rtl'])
