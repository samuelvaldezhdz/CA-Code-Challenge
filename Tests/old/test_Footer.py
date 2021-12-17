import sys
sys.path.append(sys.path[0] + "/...")
 
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import Home
import unittest
from selenium import webdriver
 

# class LM_NewsPage(WebDriverSetup):
 
#     def test_Footer(self):
#         driver = self.driver
#         self.driver.get(
#             "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
#         self.driver.set_page_load_timeout(30)
 
#         page_footer1 = "ConsumerAffairs is not a government agency. Companies displayed may pay us to be Authorized or when you click a link, call a number or fill a form on our site. Our content is intended to be used for general information purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances and consult with your own investment, financial, tax and legal advisers."
#         page_footer2 = "Company"
#         page_footer3 = "Copyright ©  2021 Consumers Unified LLC. All Rights Reserved. The contents of this site may not be republished, reprinted, rewritten or recirculated without written permission."
        
#         try:
#             if driver.footer_text1 == page_footer1:
#                 self.assertEqual(driver.footer_text1,page_footer1)
#         except AssertionError:
#             print("Assertion failed. Actual value is %s" % driver.footer_text1)
#         except Exception as error:
#             print(error+"Disclaimer failed to load")
 
#         try:
#             if driver.footer_text2 == page_footer2:
#                 self.assertEqual(driver.footer_text2,page_footer2)
#         except AssertionError:
#             print("Assertion failed. Actual value is %s" % driver.footer_text2)
#         except Exception as error:
#             print(error+"Disclaimer failed to load")   
            
#         try:
#             if driver.footer_text3 == page_footer3:
#                 self.assertEqual(driver.footer_text3,page_footer3)
#         except AssertionError:
#             print("Assertion failed. Actual value is %s" % driver.footer_text3)
#         except Exception as error:
#             print(error+"Disclaimer failed to load")
 
#         # Create an instance of the class so that you we can make use of the methods
#         # in the class
#         home_page = Home(driver)
        
        
if __name__ == '__main__':
    unittest.main()