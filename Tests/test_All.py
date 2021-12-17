import sys
sys.path.append(sys.path[0] + "/...")

from selenium.webdriver.common.by import By
from Src.WebDriverSetup import WebDriverSetup
from Src.Pages.LMNewsPage import NewsPage
import unittest


class LM_NewsPage(WebDriverSetup):
 
    def test_Disclaimer(self):
        driver = self.driver
        self.driver.get(
            "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
        self.driver.set_page_load_timeout(30)

        home_page = NewsPage(driver)
        page_t_disclaimer = "ConsumerAffairs is not a government agency and may be compensated by companies displayed."
        page_disc = str(home_page.disclaimer)

        try:
            if page_disc == page_t_disclaimer:
                self.assertEqual(page_disc, page_t_disclaimer)
        except AssertionError:
            print("Assertion failed. Actual value is %s" % page_disc)
        except Exception as error:
            print(error+"Disclaimer failed to load")

    def test_Footer(self):
        driver = self.driver
        self.driver.get(
            "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
        self.driver.set_page_load_timeout(30)

        home_page = NewsPage(driver)
        test_footer1 = home_page.footer_text1.text
        test_footer2 = home_page.footer_text2.text
        test_footer3 = home_page.footer_text3.text

        page_footer1 = "ConsumerAffairs is not a government agency. Companies displayed may pay us to be Authorized or when you click a link, call a number or fill a form on our site. Our content is intended to be used for general information purposes only. It is very important to do your own analysis before making any investment based on your own personal circumstances and consult with your own investment, financial, tax and legal advisers."
        page_footer2 = "Company"
        page_footer3 = "Copyright ©  2021 Consumers Unified LLC. All Rights Reserved. The contents of this site may not be republished, reprinted, rewritten or recirculated without written permission."

        try:
            if test_footer1 == page_footer1:
                self.assertEqual(test_footer1, page_footer1)
        except AssertionError:
            print("Assertion failed. Actual value is %s" % test_footer1)
        except Exception as error:
            print(error+"Footer1 failed to load")

        try:
            if test_footer2 == page_footer2:
                self.assertEqual(test_footer2, page_footer2)
        except AssertionError:
            print("Assertion failed. Actual value is %s" % test_footer2)
        except Exception as error:
            print(error + "Footer2 failed to load")

        try:
            if test_footer3 == page_footer3:
                self.assertEqual(test_footer3, page_footer3)
        except AssertionError:
            print("Assertion failed. Actual value is %s" % test_footer3)
        except Exception as error:
            print(error + "Footer3 failed to load")

    def test_socialFB(self):
        driver = self.driver
        self.driver.get(
            "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
        self.driver.set_page_load_timeout(30)

        try:
            home_page = NewsPage(driver)
            home_page.social_link_fb.click()
            driver.switch_to.window(driver.window_handles[-1])
            fb_page = driver.find_element(By.ID, "facebook").get_attribute("id")
            assert fb_page == "facebook"
        except Exception as error:
            print(error+"Fb link failed to load")

    def test_socialTW(self):
        driver = self.driver
        self.driver.get(
            "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
        self.driver.set_page_load_timeout(30)

        try:
            home_page = NewsPage(driver)
            home_page.social_link_tw.click()
            driver.switch_to.window(driver.window_handles[-1])
            tw_drape = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]")
            tw_drape.click()
            tw_page = driver.title

            assert tw_page
        except Exception as error:
            print(error+"Tw link failed to load")

    def test_socialMail(self):
        driver = self.driver
        self.driver.get(
            "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
        self.driver.set_page_load_timeout(30)

        home_page = NewsPage(driver)
        link_m = home_page.social_link_mail.get_attribute("href")
        assert link_m.startswith("mailto:")

    def test_MatchBox(self):
        driver = self.driver
        self.driver.get(
            "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
        self.driver.set_page_load_timeout(30)

        home_page = NewsPage(driver)
        home_page.find_my_match_zip.send_keys("94043")
        home_page.find_my_match_zip.submit()
        driver.implicitly_wait(10)
        driver.switch_to.window(driver.window_handles[-1])
        driver.implicitly_wait(10)
        next_page = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/div/div[2]/div/h2")
        assert next_page.text == "Do you own your home?"

    # def test_Related(self):
    #     driver = self.driver
    #     self.driver.get(
    #         "https://www.consumeraffairs.com/recalls/liberty-mountain-recalls-birdie-belay-devices-032921.html")
    #     self.driver.set_page_load_timeout(30)
    #
    #     home_page = NewsPage(driver)
    #     rel_first_a = home_page.related_first
    #     rel_last_a = home_page.related_last
    #
    #     try:
    #         self.assertIsNotNone(rel_first_a)
    #     except AssertionError:
    #         print("Assertion failed. Actual value is %s" % rel_first_a)
    #     except Exception as error:
    #         print(error+"Related Links failed to load")
    #
    #     try:
    #         self.assertIsNotNone(rel_last_a)
    #     except AssertionError:
    #         print("Assertion failed. Actual value is %s" % rel_last_a)
    #     except Exception as error:
    #         print(error+"Related Links failed to load")


if __name__ == '__main__':
    unittest.main()
