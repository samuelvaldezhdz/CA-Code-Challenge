import sys
sys.path.append(sys.path[0] + "/...")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())
 
import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import Home
 
# class LM_NewsPage(WebDriverSetup):
#     def test_MatchBox(self):
 
#         driver = self.driver
#         self.driver.get(
#             "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
#         self.driver.set_page_load_timeout(30)
 
#         # Create an instance of the class so that you we can make use of the methods
#         # in the class
#         home = Home(driver)
#         driver.find_my_match_zip.send_keys("94043")
#         driver.find_my_match_button.click()
#         driver.implicitly_wait(5)
#         next_page = driver.find_element_by_xpath("/html/body/div[2]/div/form/div/div[2]/div/h2")
#         assert next_page == "Do you own your home?"
        
        
 
if __name__ == '__main__':
    unittest.main()