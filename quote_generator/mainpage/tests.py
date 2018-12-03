from django.test import TestCase
from django.core.urlresolvers import resolve
from mainpage.views import main_page

class MainPageTest(TestCase):
    
    def test_root_url_returns_main_page(self):
        found = resolve('/')
        self.assertEqual(found.func, main_page)
