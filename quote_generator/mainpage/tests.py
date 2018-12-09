from django.test import TestCase
from django.urls import resolve
from mainpage.views import main_page
from django.http import request

class MainPageTest(TestCase):

    def test_root_url_returns_mainpage(self):
        response = resolve('/')
        self.assertEqual(response.func, main_page)        
    
    def test_mainpage_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main.html')
