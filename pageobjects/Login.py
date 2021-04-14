from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from .common.basepage import BASEPAGE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.general import *
import time


class Login(BASEPAGE):
    locator_dictionary = {
        "user_name": (By.ID, 'username'),
        "password": (By.ID, 'password'),
        "login_btn": (By.ID, 'Login'),
        "register_btn": (By.XPATH, './/button[@title = " Create New Profile"]'),
    }

    constants = {
        "link": '/lightning/page/home/'
    }

    def go_to(self):
        base_url = get_setting("URL", "sf_org")
        self.browser.get(base_url + self.constants["link"])
        # self.browser.get(base_url)
        try:
            WebDriverWait(self.browser, self.WAIT).until(
                EC.presence_of_element_located(self.locator_dictionary["login_btn"]))
        except:
            print("Exception: The user is not navigated to Login screen.")
        # self.click_element(self.find_element(self.locator_dictionary["atc_btn"]))
        var = self.find_element(self.locator_dictionary["login_btn"])
        assert var is not None, "The user is not navigated to Login screen."

    def login_into_website(self, user_name, password, home_screen):
        self.send_text_to_element(self.find_element(self.locator_dictionary["user_name"]), user_name)
        self.send_text_to_element(self.find_element(self.locator_dictionary["password"]), password)

        self.click_element(self.find_element(self.locator_dictionary["login_btn"]))
        try:
            WebDriverWait(self.browser, 60).until(
                EC.presence_of_element_located(self.locator_dictionary["register_btn"]))
        except:
            print("Exception: The user is not navigated to Call Center Home screen.")
        # self.click_element(self.find_element(self.locator_dictionary["atc_btn"]))
        var = self.find_element(self.locator_dictionary["register_btn"])
        assert var is not None, "The user is not navigated to Call Center Home screen."
