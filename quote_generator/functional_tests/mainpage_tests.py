#https://sites.google.com/a/chromium.org/chromedriver/home

from selenium import webdriver
import unittest

class NewMainPageVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('../../util/chromedriver.exe')
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()

        
    def test_random_quote_is_shown(self):
        self.browser.get('http://localhost:8000')
        
        #user visits the mainpage for the first time. 
        # Page title says 'Quote Generator'
        self.assertIn('Quote Generator', self.browser.title)
        # A random quote is displayed.
        quote_div = self.browser.find_element_by_id('quote-div')
        first_quote = quote_div.get_attribute("innerHTML")

        self.assertTrue(len(first_quote) > 1, "No quote found in text")

        #the user refreshes the mainpage. A new random quote is displayed.
        self.fail('finish test')

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 