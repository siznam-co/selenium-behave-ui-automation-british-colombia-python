from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from .common.basepage import BASEPAGE
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.general import *
import time


class BookAppointment(BASEPAGE):
    locator_dictionary = {
        "email_field": (By.ID, 'identifierId'),
        "next_btn": (By.XPATH, '//*[@id="identifierNext"]/div/button'),
        "password_field": (By.CSS_SELECTOR, 'input[name=password]'),
        "password_next_btn": (By.XPATH, '//*[@id="passwordNext"]/div/button'),
        "search_mail": (By.CSS_SELECTOR, 'input[placeholder="Search mail"]'),
        "search_button": (By.CSS_SELECTOR, 'button[aria-label="Search mail"]'),
        "iframe_to_be_located": (By.ID, 'gtn-roster-iframe-id'),
        "first_email": (By.XPATH, './/table/tbody/tr/td[5]/div/div/div[2]/div[1]/div/div/div'),
        "click_here_link": (By.XPATH, '(.//div/div/div/div[1]/div[2]/div[3]/div[3]/div/div[1]/a)[1]'),

        "booking_ui_widget": (By.XPATH, './/div[text()="COVID-19 Immunization"]'),
        "reg_no_field": (By.XPATH, '//*[@id="input-6"]'),
        "phn_number_field": (By.XPATH, '//*[@id="input-10"]'),
        "book_button": (By.XPATH, './/button[text() = "Book appointment"]'),
        "search_city_field": (By.XPATH, '//*[@id="input-16"]'),
        "all_cities": (By.XPATH, './/datalist/option'),
        "all_clinics": (By.XPATH, './/button[@name = "facility"]'),
        "all_days": (By.XPATH, './/button[@class = "slds-day"]'),
        "next_month_btn": (By.CSS_SELECTOR, 'button[title="Next Month"]'),
        "all_time_slots": (By.XPATH, './/button[@name="timeslot"]'),
        "appoint_next_btn": (By.XPATH, './/button[text() = "Next"]'),
        "email_checkbox": (By.XPATH, '//*[@id="email-radio-90"]'),
        "email_address": (By.XPATH, './/input[@id = "input-94"]'),
        "confirm_appoint_btn": (By.XPATH, './/button[text() = "Confirm appointment"]'),
        "appointment_confirmed_title": (By.XPATH, './/div[text() = "Appointment Confirmed!"]')
    }

    constants = {
        "link": '/mail/u/'
    }

    def go_to(self):
        base_url = get_setting("URL", "gmail")
        self.browser.get(base_url + self.constants["link"])
        # self.browser.get(base_url)
        try:
            WebDriverWait(self.browser, self.WAIT).until(
                EC.presence_of_element_located(self.locator_dictionary["email_field"]))
        except:
            print("Exception: The user is not navigated to Gamil Login screen.")
        # self.click_element(self.find_element(self.locator_dictionary["atc_btn"]))
        var = self.find_element(self.locator_dictionary["email_field"])
        assert var is not None, "The user is not navigated to Gmail Login screen."

    def login_gmail(self, email_field, password_field, home_screen):
        self.send_text_to_element(self.find_element(self.locator_dictionary["email_field"]), email_field)
        self.click_element(self.find_element(self.locator_dictionary["next_btn"]))

        self.send_text_to_element(self.find_element(self.locator_dictionary["password_field"]), password_field)
        self.click_element(self.find_element(self.locator_dictionary["password_next_btn"]))
        try:
            WebDriverWait(self.browser, 60).until(
                EC.presence_of_element_located(self.locator_dictionary["iframe_to_be_located"]))
        except:
            print("Exception: The user is not navigated to mail inbox screen.")
        # self.click_element(self.find_element(self.locator_dictionary["atc_btn"]))
        var = self.find_element(self.locator_dictionary["iframe_to_be_located"])
        assert var is not None, "The user is not navigated to mail inbox screen."

    def open_email_click_link(self, search_mail, home_screen):
        self.send_text_to_element(self.find_element(self.locator_dictionary["search_mail"]), search_mail)
        self.click_element(self.find_element(self.locator_dictionary["search_button"]))
        try:
            WebDriverWait(self.browser, 60).until(
                EC.presence_of_element_located(self.locator_dictionary["first_email"]))
        except:
            print("Exception: The user is not navigated to mail vaccination inbox screen.")

        self.click_element(self.find_element(self.locator_dictionary["first_email"]))
        self.click_element(self.find_element(self.locator_dictionary["click_here_link"]))
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        try:
            WebDriverWait(self.browser, 60).until(
                EC.presence_of_element_located(self.locator_dictionary["reg_no_field"]))
        except:
            print("Exception 2: The user is not navigated to appointment main screen.")


        # self.click_element(self.find_element(self.locator_dictionary["atc_btn"]))
        var = self.find_element(self.locator_dictionary["reg_no_field"])
        assert var is not None, "The user is not navigated to appointment main screen."

    def enter_booking_no(self, reg_no, phn_no):
        self.send_text_to_element(self.find_element(self.locator_dictionary["reg_no_field"]), reg_no)
        self.send_text_to_element(self.find_element(self.locator_dictionary["phn_number_field"]), phn_no)
        self.click_element(self.find_element(self.locator_dictionary["book_button"]))
        e = None
        try:
            e = WebDriverWait(self.browser, 60).until(
                EC.presence_of_element_located(self.locator_dictionary["search_city_field"]))
        except:
            pass
        assert e is not None, "The user is not navigated to appointment detail screen."

    def enter_booking_details(self):
        e = None
        time.sleep(2)
        # all_cities = len(self.find_elements(self.locator_dictionary["all_cities"]))
        all_cities = 67
        print("all_cities = " + str(all_cities))
        i = 1
        while all_cities >= i:
            option_loc = './/datalist/option[' + str(i) + ']'
            op = self.get_attribute(self.find_element((By.XPATH, option_loc)), 'value')
            print(op)
            self.send_text_to_element(self.find_element(self.locator_dictionary["search_city_field"]), op)
            self.click_element(self.find_element((By.XPATH, ".//h1")))
            WebDriverWait(self.browser, self.WAIT).until(EC.presence_of_element_located(self.locator_dictionary["all_clinics"]))
            i = i + 1

            all_clinics = len(self.find_elements(self.locator_dictionary["all_clinics"]))
            j = 1
            while all_clinics >= j:
                option_loc = '(.//button[@name = "facility"])[' + str(j) + ']'
                self.browser.execute_script("arguments[0].scrollIntoView(true);", self.find_element((By.XPATH, option_loc)))
                self.click_element(self.find_element((By.XPATH, option_loc)))
                WebDriverWait(self.browser, self.WAIT).until(
                    EC.presence_of_element_located(self.locator_dictionary["all_days"]))
                j = j + 1

                all_days = len(self.find_elements(self.locator_dictionary["all_days"]))
                k = 1
                while all_days >= k:
                    option_loc = '(.//button[@class = "slds-day"])[' + str(k) + ']'
                    self.browser.execute_script("arguments[0].scrollIntoView(true);", self.find_element((By.XPATH, option_loc)))
                    self.click_element(self.find_element((By.XPATH, option_loc)))
                    WebDriverWait(self.browser, self.WAIT).until(
                        EC.presence_of_element_located(self.locator_dictionary["all_time_slots"]))
                    k = k + 1

                    all_time_slots = len(self.find_elements(self.locator_dictionary["all_time_slots"]))
                    m = 1
                    while all_time_slots >= m:
                        option_loc = '(.//button[@name="timeslot"])[' + str(m) + ']'
                        self.browser.execute_script("arguments[0].scrollIntoView(true);", self.find_element((By.XPATH, option_loc)))
                        self.click_element(self.find_element((By.XPATH, option_loc)))
                        time.sleep(1)
                        m = m + 1

                        self.click_element(self.find_element(self.locator_dictionary["appoint_next_btn"]))
                        time.sleep(2)
                        try:
                            e = WebDriverWait(self.browser, self.WAIT).until(
                                EC.presence_of_element_located(self.locator_dictionary["email_address"]))
                            i = all_cities + 1
                            j = all_clinics + 1
                            k = all_days + 1
                            m = all_time_slots + 1
                        except:
                            print("Exception: The user is not navigated to appointment confirmation screen. m = " + str(
                                m))
        assert e is not None, "No appointment date/time selected."

    def confirm_booking(self, email_address):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", self.find_element(self.locator_dictionary["email_checkbox"]))
        self.click_element(self.find_element(self.locator_dictionary["email_checkbox"]))
        self.send_text_to_element(self.find_element(self.locator_dictionary["email_address"]), email_address)
        time.sleep(1)
        self.click_element(self.find_element(self.locator_dictionary["confirm_appoint_btn"]))
        e = None
        try:
            e = WebDriverWait(self.browser, 60).until(
                EC.presence_of_element_located(self.locator_dictionary["appointment_confirmed_title"]))
        except:
            pass
        assert e is not None, "The user is not navigated to appointment success screen."
