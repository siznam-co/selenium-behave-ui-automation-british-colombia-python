from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from .common.basepage import BASEPAGE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.general import *
import time


class RegisterUser(BASEPAGE):

    locator_dictionary = {
        "title_of_page": (By.XPATH, './/div[text() = "Vaccine Registration"]'),
        "register_btn": (By.XPATH, './/button/span[text() = "Register now"]'),
        "first_name": (By.XPATH, '//*[@id="input-13"]'),
        "last_name": (By.XPATH, '//*[@id="input-14"]'),
        "dob": (By.XPATH, '//*[@id="input-16"]'),
        "postal_code": (By.XPATH, '//*[@id="input-20"]'),
        "phn_number": (By.XPATH, '//*[@id="input-19"]'),
        "continue_btn": (By.XPATH, './/button[text() = "Continue"]'),
        "email_checkbox": (By.XPATH, '//*[@id="email-24"]'),
        "email_address": (By.XPATH, '//*[@id="input-25"]'),
        "confirm_email_address": (By.XPATH, '//*[@name = "ConfirmEmail"]'),
        "continue_btn_2": (By.XPATH, '(.//*/button[text() = "Continue"])[2]'),
        "patient_consent_checkbox": (By.XPATH, '//*[@id="DDH_HC_Patient_Consent-27"]'),
        "submit_btn": (By.XPATH, './/button[text() = "Submit"]'),
        "reg_number": (By.XPATH, './/div[@class = "confirmation-number"]')
    }

    constants = {
        "link": '/s/'
    }

    def go_to(self):
        base_url = get_setting("URL", "portal_url")
        self.browser.get(base_url + self.constants["link"])
        # self.browser.get(base_url)
        try:
            WebDriverWait(self.browser, self.WAIT).until(
                EC.presence_of_element_located(self.locator_dictionary["title_of_page"]))
        except:
            print("Exception: The user is not navigated to Portal Home screen.")
        # self.click_element(self.find_element(self.locator_dictionary["atc_btn"]))
        var = self.find_element(self.locator_dictionary["title_of_page"])
        assert var is not None, "The user is not navigated to Portal Home screen."

    def click_register_btn(self, register_btn):
        e = ""
        self.click_element(self.find_element(self.locator_dictionary["register_btn"]))
        try:
            e = WebDriverWait(self.browser, self.WAIT).until(
                    EC.presence_of_element_located(self.locator_dictionary["continue_btn"]))
        except:
            print("The form is not appeared.")
        assert e is not None, "The form is not appeared."

    def fill_form_step_one(self, first_name, last_name, dob, postal_code, phn_number):
        e = ""
        self.send_text_to_element(self.find_element(self.locator_dictionary["first_name"]), first_name)
        self.send_text_to_element(self.find_element(self.locator_dictionary["last_name"]), last_name)
        self.send_text_to_element(self.find_element(self.locator_dictionary["dob"]), dob)
        self.send_text_to_element(self.find_element(self.locator_dictionary["postal_code"]), postal_code)
        self.send_text_to_element(self.find_element(self.locator_dictionary["phn_number"]), phn_number)

        self.click_element(self.find_element(self.locator_dictionary["continue_btn"]))
        time.sleep(1)
        try:
            e = WebDriverWait(self.browser, self.WAIT).until(
                    EC.presence_of_element_located(self.locator_dictionary["continue_btn_2"]))
        except:
            print("The form is not appeared.")
        assert e is not None, "The form step 2 is not appeared."

    def fill_form_step_two(self, email):
        e = ""
        self.click_element(self.find_element(self.locator_dictionary["email_checkbox"]))
        self.send_text_to_element(self.find_element(self.locator_dictionary["email_address"]), email)
        self.send_text_to_element(self.find_element(self.locator_dictionary["confirm_email_address"]), email)

        self.click_element(self.find_element(self.locator_dictionary["continue_btn_2"]))
        try:
            e = WebDriverWait(self.browser, self.WAIT).until(
                    EC.presence_of_element_located(self.locator_dictionary["submit_btn"]))
        except:
            print("The form is not appeared.")
        assert e is not None, "The form step 3 is not appeared."

    def submit_form(self, consent_btn, submit_btn):
        e = ""
        time.sleep(2)
        self.click_element(self.find_element(self.locator_dictionary["patient_consent_checkbox"]))
        time.sleep(1)
        self.click_element(self.find_element(self.locator_dictionary["submit_btn"]))
        try:
            e = WebDriverWait(self.browser, self.WAIT).until(
                    EC.presence_of_element_located(self.locator_dictionary["reg_number"]))
        except:
            print("The form was not submitted. Try Again!")
        assert e is not None, "The form was not submitted. Try Again!"

    def save_reg_number(self, reg_number):
        r = self.get_element_text(self.find_element(self.locator_dictionary["reg_number"]))
        r = r.replace(" ", "")
        print(r)
        return r

