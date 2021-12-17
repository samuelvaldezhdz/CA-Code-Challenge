import sys
sys.path.append(sys.path[0] + "/...")
 
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import Home
import unittest
from selenium import webdriver
 

# class LM_NewsPage(WebDriverSetup):
 
#     def test_socialFB(self):
#         driver = self.driver
#         self.driver.get(
#             "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
#         self.driver.set_page_load_timeout(30)
        
#         try:
#             driver.social_link_fb.click()
            
#             if driver.disclaimer == page_disclaimer:
#                 self.assertEqual(driver.disclaimer,page_disclaimer)
#         except AssertionError:
#             print("Assertion failed. Actual value is %s" % driver.disclaimer)
#         except Exception as error:
#             print(error+"Disclaimer failed to load")
 
#         # Create an instance of the class so that you we can make use of the methods
#         # in the class
#         home_page = Home(driver)
        
        
if __name__ == '__main__':
    unittest.main()