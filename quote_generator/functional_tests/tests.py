#https://sites.google.com/a/chromium.org/chromedriver/home

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
class NewMainPageVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('../util/chromedriver.exe')
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()

        
    def test_random_quote_is_shown(self):
        self.browser.get(self.live_server_url)
        
        #user visits the mainpage for the first time. 
        # Page title says 'Quote Generator'
        self.assertIn('Quote Generator', self.browser.title)
        # A random quote is displayed.
        first_quote = self.browser.find_element_by_id('quote-div').text
        first_author = self.browser.find_element_by_id('quote-author').text

        self.assertNotEqual(first_quote, '', 'No quote found!')
        self.assertNotEqual(first_author.strip(), '-', 'No author found!')

        #the user refreshes the mainpage. A new random quote is displayed.
        self.browser.refresh()
        second_quote = self.browser.find_element_by_id('quote-div').text
        second_author = self.browser.find_element_by_id('quote-author').text

        self.assertNotEqual(second_quote, '', 'No quote found!')
        self.assertNotEqual(second_quote, first_quote, 'Expected a new quote!')
        self.assertNotEqual(second_author.strip(), '-', 'No author found!')