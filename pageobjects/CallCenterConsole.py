from pyshadow.main import Shadow
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
                                  'COVID_19_Vaccination."]'),

        "parent_in_dom": (By.ID, 'brandBand_2'),
        "all_tabs": (By.XPATH,
                     '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/one-record-home-flexipage2/forcegenerated-adgrollup_component___forcegenerated__flexipage_recordpage___hc_participant_record_page22___account___view/forcegenerated-flexipage_hc_participant_record_page22_account__view_js/record_flexipage-record-page-decorator/div[1]/slot/flexipage-record-home-template-desktop2/div/div[2]/div[1]'),
        "appointment_tab": (By.XPATH, './/a[@id = "customTab__item"]'),
        "appointment_title": (By.XPATH, './/strong[text() = "Patient Appointment Scheduling"]'),
        "covid_vaccination_option_2": (By.XPATH, './/select/option[text() = "COVID-19 Vaccination"]'),
        "all_cities": (By.XPATH, '(.//select)[2]/option'),
        "all_clinics": (By.XPATH, '(.//select)[3]/option'),
        "all_cities_dropdown": (By.XPATH, '(.//select)[2]'),
        "all_clinics_dropdown": (By.XPATH, '(.//select)[3]'),
        "search_btn": (By.XPATH, './/button[@title = "Search"]'),
        "all_select_btns": (By.XPATH, './/button[@title = "Select"]'),
        "save_btn": (By.XPATH, './/button[@title = "Save"]'),
        "success_toast_2": (By.XPATH, './/div[text() = "Success!"]'),
        "sgi_booking_link": (By.XPATH, './/a[contains(text(), "SGI-")]'),
        "appointment_number": (By.XPATH, './/slot/force-highlights-details-item[1]/div/p['
                                         '2]/slot/lightning-formatted-text')
    }

    constants = {
        "link": '/lightning/page/home/'
    }

    def __init__(self, context):
        super().__init__(context)

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
        self.set_current_window_handle(self.browser.current_window_handle)

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
        e = None
        time.sleep(1)
        self.click_element(self.find_element(self.locator_dictionary["register_btn_last"]))
        try:
            e = WebDriverWait(self.browser, self.WAIT).until(
                EC.presence_of_element_located(self.locator_dictionary["check_eligibility_btn"]))
        except:
            print("The form was not submitted. Try Again!")
        assert e is not None, "The form was not submitted. Try Again!"

    def expand_shadow_element(self, element):
        shadow_root = self.browser.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    window_before = None

    def set_current_window_handle(self, wb):
        CallCenterConsole.windows_before = wb
        return CallCenterConsole.windows_before

    def get_current_window_for_click(self):
        windows_before = CallCenterConsole.window_before
        # WebDriverWait(self.browser, 10).until(EC.number_of_windows_to_be(2))
        windows_after = self.browser.window_handles
        new_window = [x for x in windows_after if x != windows_before][0]
        self.browser.switch_to.window(new_window)
        # get the Session id of the Parent
        # parentGUID = self.browser.current_window_handle
        # # get the All the session id of the browsers
        # allGUID = self.browser.window_handles
        # print(allGUID)
        # num = len(allGUID)
        # print(str(num))
        # w = self.browser.window_handles[num - 1]
        # self.browser.switch_to.window(str(allGUID[2]))
        # i = 0
        # while num != 0:
        #     # one enter into if block if the GUID is not equal to parent window's GUID
        #     if allGUID[i] == parentGUID:
        #         # switch to the guid
        #         self.browser.switch_to.window(guid)
        #         # break the loop
        #         break

    def go_to_appointment_tab(self):
        e = None
        # Getting the current open tab/window
        # self.get_current_window_for_click()
        current_url = self.browser.current_url
        self.browser.get(current_url)
        # self.browser.switch_to.window(self.browser.window_handles[-1])
        try:
            e = WebDriverWait(self.browser, 50).until(
                EC.presence_of_element_located(self.locator_dictionary["check_phn_btn"]))
        except:
            print("The citizen list screen is not appeared.")

        time.sleep(2)
        e = self.find_element(self.locator_dictionary["appointment_tab"])
        e.click()
        try:
            WebDriverWait(self.browser, self.WAIT).until(
                EC.presence_of_element_located(self.locator_dictionary["appointment_title"]))
        except:
            print("Exception: The user is not navigated to citizen appointment screen.")
            self.browser.execute_script("arguments[0].click();",
                                        self.find_element(self.locator_dictionary["appointment_tab"]))
        # self.click_element(self.find_element(self.locator_dictionary["atc_btn"]))
        var = self.find_element(self.locator_dictionary["appointment_title"])
        assert var is not None, "The user is not navigated to citizen appointment screen."

    def search_and_select_appointment(self):

        self.click_element(self.find_element(self.locator_dictionary["covid_vaccination_option_2"]))

        time.sleep(2)
        # self.click_element(self.find_elements(self.locator_dictionary["all_cities_dropdown"]))
        # time.sleep(1)
        all_cities = len(self.find_elements(self.locator_dictionary["all_cities"])) - 1
        print(str(all_cities))
        i = 2
        while all_cities >= i:
            option_loc = '(.//select)[2]/option[' + str(i) + ']'
            self.click_element(self.find_element((By.XPATH, option_loc)))
            time.sleep(2)
            i = i + 1
            # self.click_element(self.find_elements(self.locator_dictionary["all_clinics_dropdown"]))
            # time.sleep(1)
            all_clinics = len(self.find_elements(self.locator_dictionary["all_clinics"])) - 1
            print(str(all_clinics))

            j = 2
            while all_clinics >= j:
                option_loc = '(.//select)[3]/option[' + str(j) + ']'
                self.click_element(self.find_element((By.XPATH, option_loc)))
                time.sleep(1)
                j = j + 1

                self.browser.execute_script("arguments[0].click();", self.find_element(self.locator_dictionary["search_btn"]))
                # self.click_element(self.find_element(self.locator_dictionary["search_btn"]))
                time.sleep(2)

                all_select_btns = len(self.find_elements(self.locator_dictionary["all_select_btns"]))
                k = 1
                while all_select_btns >= k:
                    select_btn_loc = '(.//button[@title = "Select"])[' + str(k) + ']'
                    print("K = " + str(k))
                    self.click_element(self.find_element((By.XPATH, select_btn_loc)))
                    try:
                        WebDriverWait(self.browser, self.WAIT).until(
                            EC.presence_of_element_located(self.locator_dictionary["save_btn"]))
                        i = all_cities + 1
                        j = all_clinics + 1
                        k = all_select_btns + 1
                    except:
                        print("Exception: The user is not navigated to appointment confirmation screen.")
                        k = k + 1

    def save_appointment(self):
        self.browser.execute_script("arguments[0].click();", self.find_element(self.locator_dictionary["save_btn"]))
        # self.click_element(self.find_element(self.locator_dictionary["save_btn"]))
        try:
            e = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(self.locator_dictionary["success_toast_2"]))
        except:
            print("Exception: The form was not submitted. Try Again!")
        e = self.find_element(self.locator_dictionary["success_toast_2"])
        assert e is not None, "The appointment was not submitted. Try Again!"

    def get_appointment_number(self):
        self.browser.execute_script("arguments[0].click();", self.find_element(self.locator_dictionary["sgi_booking_link"]))
        # self.click_element(self.find_element(self.locator_dictionary["sgi_booking_link"]))
        try:
            e = WebDriverWait(self.browser, 20).until(
                EC.presence_of_element_located(self.locator_dictionary["appointment_number"]))
        except:
            print("Exception: The user is not navigated to appointment screen. Try Again!")
        e = self.find_element(self.locator_dictionary["appointment_number"])
        assert e is not None, "The user is not navigated to appointment screen"
        print("The citizen appointment number is: " + self.get_element_text(e))
        time.sleep(5)
