from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from .common.basepage import BASEPAGE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.general import *
import time


class CallCenterConsole(BASEPAGE):

    locator_dictionary = {
        "register_btn": (By.XPATH, './/button[@title = " Create New Profile"]'),
        "title_of_page": (By.XPATH, './/div[text() = "Citizen\'s Primary Information"]'),

        "first_name": (By.XPATH, '//*[@name="FirstName"]'),
        "last_name": (By.XPATH, '//*[@name="LastName"]'),
        "dob": (By.XPATH, '//*[@name="PersonBirthdate"]'),
        "postal_code": (By.XPATH, '//*[@name="DDH_HC_Zip_Code"]'),
        "phn_number": (By.XPATH, '//*[@name="HC_Personal_Health_Number"]'),
        "check_phn_btn": (By.XPATH, './/button[@title = "Verify Personal Health Number"]'),
        "phn_un_success_toast": (By.XPATH, './/h2[text() = "Data Match Unsuccessful"]'),
        "phn_cancel_btn": (By.XPATH, './/button[@title = "Cancel"]'),
        "next_btn": (By.XPATH, './/button[@title = "Next"]'),
        "email_checkbox": (By.XPATH, '//*[@name="DDH_HC_Preferred"]'),
        "email_address": (By.XPATH, '//*[@name="PersonEmail"]'),
        "confirm_email_address": (By.XPATH, '//*[@name = "ConfirmEmail"]'),
        "review_btn": (By.XPATH, './/button[@title = "Review"]'),

        "register_btn_last": (By.XPATH, './/button[text() = "Register"]'),

        "reg_number": (By.XPATH, './/div[@class = "confirmation-number"]'),

        "global_search_field": (By.XPATH, './/input[@placeholder = "Search..."]'),
        "search_icon": (By.XPATH, '(.//li[@role = "presentation"])'),
        "searched_citizen": (By.XPATH, './/tbody/tr/th/span/a'),
        "check_eligibility_btn": (By.XPATH, './/button[@title = "Check Eligibility"]'),
        "success_toast": (By.XPATH, './/div[text() = "Success"]'),
        "covid_vaccination_option": (By.XPATH, './/select[@name = "typeId"]/option[text() = "COVID_19_Vaccination"]'),
        "is_eligible": (By.XPATH, './/span[text() = "Eligibility check completed. Participant is eligible for '
                                  'COVID_19_Vaccination."]')

    }

    constants = {
        "link": '/lightning/page/home/'
    }

    def check_reg_no(self, reg_no):
        self.send_text_to_element(self.find_element(self.locator_dictionary["global_search_field"]), reg_no)
        time.sleep(2)
        WebDriverWait(self.browser, self.WAIT).until(
            EC.presence_of_element_located(self.locator_dictionary["search_icon"])).click()
        time.sleep(2)
        try:
            WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(self.locator_dictionary["searched_citizen"]))
        except:
            print("The search field is not working.")
        # self.click_element(self.find_element(self.locator_dictionary["atc_btn"]))
        var = self.find_element(self.locator_dictionary["searched_citizen"])
        assert var is not None, "The searched record(s) are not displayed."

    def open_patient_record(self):
        self.click_element(self.find_element(self.locator_dictionary["searched_citizen"]))
        try:
            WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(self.locator_dictionary["check_eligibility_btn"]))
        except:
            print("Exception: The records in not clickable at the moment")
        # self.click_element(self.find_element(self.locator_dictionary["atc_btn"]))
        var = self.find_element(self.locator_dictionary["check_eligibility_btn"])
        assert var is not None, "The opened record is not displayed."

    def check_eligibility(self):
        # self.click_element(self.find_element(self.locator_dictionary["check_eligibility_btn"]))
        self.browser.execute_script("arguments[0].click();",
                                    self.find_element(self.locator_dictionary["check_eligibility_btn"]))
        self.click_element(self.find_element(self.locator_dictionary["covid_vaccination_option"]))
        try:
            WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(self.locator_dictionary["is_eligible"]))
        except:
            print("Exception: The records in not clickable at the moment")
        # self.click_element(self.find_element(self.locator_dictionary["atc_btn"]))
        var = self.find_element(self.locator_dictionary["is_eligible"])
        assert var is not None, "The opened record is not displayed."
        time.sleep(5)

    def click_register_btn(self, register_btn):
        e = ""
        self.click_element(self.find_element(self.locator_dictionary["register_btn"]))
        try:
            e = WebDriverWait(self.browser, self.WAIT).until(
                    EC.presence_of_element_located(self.locator_dictionary["title_of_page"]))
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

        self.click_element(self.find_element(self.locator_dictionary["first_name"]))

        self.click_element(self.find_element(self.locator_dictionary["check_phn_btn"]))

        if self.is_element_displayed(self.locator_dictionary["success_toast"]):
            time.sleep(2)
        else:
            e = self.find_element(self.locator_dictionary["phn_un_success_toast"])
            if e is not None:
                self.click_element(self.find_element(self.locator_dictionary["phn_cancel_btn"]))
            else:
                print("The phn number is not verified.")
        self.click_element(self.find_element(self.locator_dictionary["next_btn"]))
        time.sleep(1)
        try:
            e = WebDriverWait(self.browser, self.WAIT).until(
                    EC.presence_of_element_located(self.locator_dictionary["review_btn"]))
        except:
            print("The form is not appeared.")
        assert e is not None, "The form step 2 is not appeared."

    def fill_form_step_two(self, email):
        e = ""
        self.click_element(self.find_element(self.locator_dictionary["email_checkbox"]))
        self.send_text_to_element(self.find_element(self.locator_dictionary["email_address"]), email)
        self.send_text_to_element(self.find_element(self.locator_dictionary["confirm_email_address"]), email)

        self.click_element(self.find_element(self.locator_dictionary["review_btn"]))
        try:
            e = WebDriverWait(self.browser, self.WAIT).until(
                    EC.presence_of_element_located(self.locator_dictionary["register_btn_last"]))
        except:
            print("The form is not appeared.")
        assert e is not None, "The form step 3 is not appeared."

    def submit_form(self, submit_btn):
        e = ""
        time.sleep(1)
        self.click_element(self.find_element(self.locator_dictionary["register_btn_last"]))
        try:
            e = WebDriverWait(self.browser, self.WAIT).until(
                    EC.presence_of_element_located(self.locator_dictionary["check_eligibility_btn"]))
        except:
            print("The form was not submitted. Try Again!")
        assert e is not None, "The form was not submitted. Try Again!"
