import sys
sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from Src.Locators import Locator

 
class NewsPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.disclaimer = driver.find_element(By.XPATH, Locator.disclaimer)
        self.footer_text1 = driver.find_element(By.XPATH, Locator.footer_text1)
        self.footer_text2 = driver.find_element(By.XPATH, Locator.footer_text2)
        self.footer_text3 = driver.find_element(By.XPATH, Locator.footer_text3)
        self.social_link_fb = driver.find_element(By.XPATH, Locator.social_link_fb)
        self.social_link_tw = driver.find_element(By.XPATH, Locator.social_link_tw)
        self.social_link_mail = driver.find_element(By.XPATH, Locator.social_link_mail)
        self.find_my_match_zip = driver.find_element(By.XPATH, Locator.find_my_match_zip)
        # self.related_first = driver.find_element(By.XPATH, Locator.rel_first)
        # self.related_last = driver.find_element(By.XPATH, Locator.rel_last)

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

    # def getRelatedFirst(self):
    #     return self.related_first
    #
    # def getRelatedLast(self):
    #     return self.related_last

    
    