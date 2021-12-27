from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement

class BaseDriver:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def scroll_to_bottom_page(self):
        """
        Description: Scroll to the bottom of page
        """
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

    def scroll_to_element(self, xpath: str):
        """
        Description: Scroll to the element
        """
        element: WebElement = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_presence_of_all_elements(self, locator):
        list_of_element = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
        return list_of_element

    def wait_until_element_to_be_clickable(self, locator):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        return element

    def wait_and_set_text_with_clear(self, locator: str, text_value: str):
        """
        Description: Wait element is visibility then send key
        :param xpath:
        :param text_value:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
            element.clear()
            element.send_keys(text_value)
        except Exception as exc:
            raise Exception("Element cannot located!" + "\n" + str(exc))

    def wait_and_set_text_and_enter(self, locator: str, text_value: str):
        """
        Description: Wait element is visibility then send key
        :param xpath:
        :param text_value:
        :param time_out:
        :return:
        """
        try:
            element: WebElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
            element.click()
            element.send_keys(text_value)
            element.send_keys(Keys.ENTER)
        except Exception as exc:
            raise Exception("Element cannot located!" + "\n" + str(exc))


    def wait_and_click_element(self, locator: str):
        """
        Description: Wait until element can click able, then click element
        :param driver: Web Driver
        :param xpath: xpath for this element
        :param time_out: time for implicitly wait
        :return:
        """
        try:
            element: WebElement = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
            element.click()
        except Exception as exc:
            raise Exception("Element cannot clickable!" + "\n" + str(exc))