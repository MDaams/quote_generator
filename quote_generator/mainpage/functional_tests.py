#https://sites.google.com/a/chromium.org/chromedriver/home

from selenium import webdriver
import unittest

class NewMainPageVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('../util/chromedriver.exe')
    
    def tearDown(self):
        self.browser.quit()