import time

from behave import *
import pandas as pd

from pageobjects.BookAppointment import BookAppointment
from pageobjects.CallCenterConsole import CallCenterConsole
from pageobjects.Login import Login
from pageobjects.RegisterUser import RegisterUser, get_setting, set_setting


@given("user is on Citizen portal HOME page")
def step_impl(context):
    RegisterUser(context).go_to()


@when('the user clicks "{register_btn}" button, the user is navigated to a 3 step form screen.')
def step_impl(context, register_btn):
    RegisterUser(context).click_register_btn(register_btn)


@then('the user fills the personal details and click "{continue_btn}" button.')
def step_impl(context, continue_btn):
    # df = pd.read_csv('data.csv')
    df = pd.read_csv('data.csv', header=None, nrows=5)
    print(df[0][1])
    RegisterUser(context).fill_form_step_one("BEATRICE", "BCYPCST", "Jan 25, 1932", "V0R2Y0", "9879454689")


@step('the user enters the "{email}" or "{sms_phone_number}" to send confirmation and click "{continue_btn}" button.')
def step_impl(context, email, sms_phone_number, continue_btn):
    RegisterUser(context).fill_form_step_two(get_setting("EMAIL", "email"))


@then('the user verify all the detail provided, hit "{consent_btn}" button and clicks "{submit_btn}" button to submit '
      'the registration successfully.')
def step_impl(context, consent_btn, submit_btn):
    RegisterUser(context).submit_form(consent_btn, submit_btn)


@step('the user copies "{reg_number}" and save it.')
def step_impl(context, reg_number):
    reg = RegisterUser(context).save_reg_number(reg_number)
    set_setting("REG_NO", "reg_no", reg)


@given("user is on Login Page.")
def step_impl(context):
    Login(context).go_to()


@when('the user provide the "{user_name}" and "{password}", and clicks the "{login_btn}" button, the user is '
      'navigated to the "{home_screen}" screen.')
def step_impl(context, user_name, password, login_btn, home_screen):
    Login(context).login_into_website(get_setting("CRED", "username"), get_setting("CRED", "password"), home_screen)


@then("the user search with citizen with his/her registration number and check if the record is there or not.")
def step_impl(context):
    CallCenterConsole(context).check_reg_no(get_setting("REG_NO", "reg_no"))


@step("the clicks and opens the user record.")
def step_impl(context):
    CallCenterConsole(context).open_patient_record()


@then('the user clicks on the "{check_eligibility_btn}" button, selects the "{vaccination_option}" option and check '
      'if the patient is eligible.')
def step_impl(context, check_eligibility_btn, vaccination_option):
    CallCenterConsole(context).check_eligibility()


@when('the user clicks "{reg_btn}" button, the user is navigated to 3 step form screen.')
def step_impl(context, reg_btn):
    CallCenterConsole(context).click_register_btn(reg_btn)


@then('the user fills the personal details, verify "{phn_number}" number and clicks "{next_btn}" button.')
def step_impl(context, phn_number, next_btn):
    CallCenterConsole(context).fill_form_step_one("BEATRICE", "BCYPCST", "Jan 25, 1932", "V0R2Y0", "9879454689")


@step('the user enters the "{email}" or "{sms_phone_number}" to send confirmation email and click "{review_btn}" '
      'button.')
def step_impl(context, email, sms_phone_number, review_btn):
    CallCenterConsole(context).fill_form_step_two(get_setting("EMAIL", "email"))


@then('the user verify all the details provided, and clicks "{register_btn}" button to submit the registration '
      'successfully.')
def step_impl(context, register_btn):
    CallCenterConsole(context).submit_form(register_btn)


@step("if the user is eligible, go the {appointment} tab of the citizen list screen.")
def step_impl(context, appointment):
    CallCenterConsole(context).go_to_appointment_tab()


@when("the user selects {vaccine}, {city} and {hospital}, and click {select} button on available slots.")
def step_impl(context, vaccine, city, hospital, select):
    CallCenterConsole(context).search_and_select_appointment()


@then("the user {saves} the appointment after reviewing.")
def step_impl(context, saves):
    CallCenterConsole(context).save_appointment()


@step("clicks the provides {sgi_number} number to go to the {appointment_list} screen to verify the {"
      "appointment_confirmation_number}.")
def step_impl(context, sgi_number, appointment_list, appointment_confirmation_number):
    CallCenterConsole(context).get_appointment_number()


@given("user is on email {login_page} Page.")
def step_impl(context, login_page):
    BookAppointment(context).go_to()


@when('the user provide the "{user_name}" and "{password}", and clicks the "{login_btn}" button, the user is '
      'navigated to the mail "{inbox}" screen.')
def step_impl(context, user_name, password, login_btn, inbox):
    BookAppointment(context).login_gmail(get_setting("EMAIL", "email"), get_setting("EMAIL", "pw"), inbox)


@then("the user opens the received email and click the link {click_here_link} which will take the user to the {"
      "appointment} screen.")
def step_impl(context, click_here_link, appointment):
    BookAppointment(context).open_email_click_link("label:vaccination-confirmation", appointment)


@when("the user clicks {book_appointment} button after entering {registration_confirmation_number} and {phn_number}, "
      "the user is moved to appointment detail screen.")
def step_impl(context, book_appointment, registration_confirmation_number, phn_number):
    BookAppointment(context).enter_booking_no(get_setting("REG_NO", "reg_no"), '9879454689')


@step("the user selects the {appointment_details} and clicks {next_btn} button.")
def step_impl(context, appointment_details, next_btn):
    BookAppointment(context).enter_booking_details()


@then("the user enters email and confirm booking.")
def step_impl(context):
    BookAppointment(context).confirm_booking(get_setting("EMAIL", "email"))
