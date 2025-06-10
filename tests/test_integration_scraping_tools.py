import unittest

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium_crawler.scraping_tools import get_element
from selenium_crawler.webdrivercreator import create_webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class TestIntegrationScrapingTools(unittest.TestCase):

    def test_bot_detection_site(self):
        driver = None
        try:
            driver = create_webdriver(False)
            driver.get("https://bot.sannysoft.com/")

            self.assert_test(
                driver, (By.XPATH, "//td[@id='user-agent-result']"))
            #self.assert_test(
            #    driver, (By.XPATH, "//td[@id='webdriver-result']"))
            self.assert_test(
                driver, (By.XPATH, "//td[@id='advanced-webdriver-result']"))
            self.assert_test(
                driver, (By.XPATH, "//td[@id='chrome-result']"))
            self.assert_test(
                driver, (By.XPATH, "//td[@id='permissions-result']"))
            self.assert_test(
                driver, (By.XPATH, "//td[@id='plugins-length-result']"))
            self.assert_test(
                driver, (By.XPATH, "//td[@id='permissions-result']"))
            self.assert_test(
                driver, (By.XPATH, "//td[@id='languages-result']"))
            self.assert_test(
                driver, (By.XPATH, "//td[@id='webgl-vendor']"))
            self.assert_test(
                driver, (By.XPATH, "//td[@id='webgl-renderer']"))
            self.assert_test(
                driver, (By.XPATH, "//td[@id='broken-image-dimensions']"))
        finally:
            if driver:
                driver.quit()

    def test_bot_score(self):
        driver = None
        try:
            driver = create_webdriver(False)
            driver.get("https://fingerprint-scan.com/")
        finally:
            if driver:
                driver.quit()

    def assert_test(self, driver: WebDriver, locator: tuple[str, str]) -> None:
        try:
            elements = get_element(driver, locator)
            # check if element has a class attribute that contains 'passed'
            attribute = elements.get_attribute('class')
            if attribute == 'result passed' or attribute == 'passed':
                assert True
            else:
                assert False, (
                    f"element {locator[1]} found but does not have the expected class: {attribute}")
        except TimeoutException:
            assert False, f"element {locator[1]} not found within the timeout period."
