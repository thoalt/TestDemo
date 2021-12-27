import logging
import time

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import BaseDriver
from utilites.utils import Utils

class SeachFligthResults(BaseDriver):
    log = Utils.loggen(logLevel=logging.INFO)
    def __init__(self, driver):
        super().__init__(driver)

    ONE_STOP_XPATH = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    TWO_STOP_XPATH = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    NONE_STOP_XPATH = "//p[@class='font-lightgrey bold'][normalize-space()='0']"

    def filter_flights_by_stops(self, stop_val):
        if stop_val == "1 Stop":
            self.wait_and_click_element(self.ONE_STOP_XPATH)
            self.log.info("Selected flight with 1 stop")
        elif stop_val == "2 Stop":
            ele = self.wait_and_click_element(self.TWO_STOP_XPATH)
            self.log.info("Selected flight with 2 stop")
        elif stop_val == "0 Stop":
            self.wait_and_click_element(self.NONE_STOP_XPATH)
            self.log.info("Other selected")
        time.sleep(4)

    def get_search_fligth_results(self):
        return self.wait_for_presence_of_all_elements("//span[contains(text(), '1 Stop')]")


