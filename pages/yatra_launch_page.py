import time

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import BaseDriver
from pages.search_flight_results_page import SeachFligthResults
from utilites.utils import Utils


class LauchPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)

    log = Utils.loggen()
    # Locator
    DEPART_FROM_XPATH = "//input[@id='BE_flight_origin_city']"
    GOING_LOCATION_XPATH = "//input[@id='BE_flight_arrival_city']"
    SEARCH_RESULT = "//div[@class='viewport']//div[1]/li"
    SELETCT_DATE_XPATH = "//input[@id='BE_flight_origin_date']"
    ALLDATE_XPATH = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    DATE_INACTIVATE_XPATH = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    CLICK_BUTTON_XPATH = "//input[@value='Search Flights']"

    def setDepartfrom(self, departlocation):
        depart = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.DEPART_FROM_XPATH)))
        depart.click()
        depart.send_keys(departlocation)
        depart.send_keys(Keys.ENTER)
        #self.wait_and_set_text_and_enter(self.DEPART_FROM_XPATH, departlocation)
        time.sleep(2)

    def setGoingto(self, goinglocation):
        # self.wait_and_click_element(self.GOING_LOCATION_XPATH)
        going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.GOING_LOCATION_XPATH)))
        going_to.click()
        time.sleep(2)
        going_to.send_keys(goinglocation)
        search_result = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.SEARCH_RESULT)))
        for results in search_result:
            if goinglocation in results.text:
                results.click()
                break


    def selectdate(self, departuredate):
        self.wait_and_click_element(self.SELETCT_DATE_XPATH)

        #select_date.click()
        all_dates = self.wait_until_element_to_be_clickable(self.ALLDATE_XPATH)\
                        .find_elements(By.XPATH, self.DATE_INACTIVATE_XPATH)
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    def clickSearch(self):
        self.wait_and_click_element(self.CLICK_BUTTON_XPATH)
        time.sleep(5)

    def searchFlights(self, departlocation, goinglocation, departuredate):
        self.log.info("Set Department")
        print(departlocation)
        self.setDepartfrom(departlocation)

        self.log.info("Set Going To")
        print(goinglocation)
        self.setGoingto(goinglocation)
        time.sleep(2)

        self.selectdate(departuredate)
        self.clickSearch()
        search_fly_result = SeachFligthResults(self.driver)
        return search_fly_result