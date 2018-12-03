#https://sites.google.com/a/chromium.org/chromedriver/home

from selenium import webdriver
import unittest

class NewMainPageVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('../../util/chromedriver.exe')
    
    def tearDown(self):
        self.browser.quit()

        
    def test_random_quote_is_shown(self):
        self.browser.get('http://localhost:8000')
        #user visits the mainpage for the first time. 
        # Page title says 'Quote Generator'
        self.assertIn('Quote Generator', self.browser.title)
        # A random quote is displayed.
        quote_div = driver.find_element_by_id('quote-div')
        time.sleep(5)
        #the user refreshes the mainpage. A new random quote is displayed.
        self.fail('finish test')

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 