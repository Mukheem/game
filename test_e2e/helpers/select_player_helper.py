'''
1. import statement
2.object creations
commonhelper()

1.element locators



1.functions
'''
# creating object for common helper class
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# ch = commonHelper() // Object Creation
class select_player:

    def __init__(self, driver):
        self.driver = driver

    blue_button = "//div[@class='container app-body-content']/div/button[1]"
    red_button = "//div[@class='container app-body-content']/div/button[2]"

    def click_blue_button(self):
        from test_e2e.common.common_helper import common_helper
        ch = common_helper(self.driver)
        ch.click_element(self.blue_button, 15, 0.5)

    def click_red_button(self):
        from test_e2e.common.common_helper import common_helper
        ch = common_helper(self.driver)

    # def click_drop_button(self):
    #     from test_e2e.common.common_helper import common_helper
    #     ch = common_helper(self.driver)
