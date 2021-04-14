import time

from behave import *
import pandas as pd

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
    RegisterUser(context).fill_form_step_one("BEATRICE", "BCYPCST", "Jan 25, 1932", "9879454689", "V0R2Y0")


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