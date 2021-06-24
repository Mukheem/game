import time

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



@pytest.mark.usefixtures("setUp")
class common_helper:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, element , timeout=10, frequency=0.5):
        '''
        This method is a common method which we use to click a web element across framework

        '''
        try:

            wait = WebDriverWait(self.driver, timeout =timeout, poll_frequency= frequency)  # timeout in seconds -> 30
            wait.until(EC.element_to_be_clickable((By.XPATH, element)))
            self.driver.find_element_by_xpath(element).click()
            time.sleep(5000)
        except Exception as e:
            print(e)

    def is_present(self, element, timeout=10, frequency=0.5):
            '''
            This method is a common method validate if the correct data is displayed or not

            '''
            try:

                wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=frequency)  # timeout in seconds -> 30
                wait.until(EC.presence_of_element_located)
                self.driver.find_element_by_xpath(element).is_displayed()

            except Exception as e:
                print(e)
