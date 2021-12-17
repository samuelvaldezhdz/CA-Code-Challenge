import sys
sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())
 
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator

 
class TwPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.disclaimer = driver.find_element(By.XPATH, Locator.disclaimer)
        
        
    def getDisclaimer(self):
        return self.disclaimer
 
    def getFooterText1(self):
        return self.footer_text1
    
    def getFooterText2(self):
        return self.footer_text2
    
    def getFooterText3(self):
        return self.footer_text3
 
    def getSocialFB(self):
        return self.social_link_fb
    
    def getSocialTW(self):
        return self.social_link_tw
    
    def getSocialMail(self):
        return self.social_link_mail
    
    def getMatchZip(self):
        return self.find_my_match_zip
    
    def getMatchButton(self):
        return self.find_my_match_button
    
    def getRelatedFirst(self):
        return self.related_first
    
    def getRelatedLast(self):
        return self.related_last
    
    
    