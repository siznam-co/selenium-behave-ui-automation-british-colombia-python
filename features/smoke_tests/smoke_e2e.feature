Feature: Vaccine Registration

  @reg_thru_portal
  Scenario: Register a citizen through portal.
    Given user is on Citizen portal HOME page
    When the user clicks "Register" button, the user is navigated to a 3 step form screen.
    Then the user fills the personal details and click "Continue" button.
    And the user enters the "email" or "sms phone number" to send confirmation and click "Continue" button.
    Then the user verify all the detail provided, hit "consent" button and clicks "Submit" button to submit the registration successfully.
    And the user copies "registration confirmation number" and save it.

  @search_reg_in_call_center
  Scenario: Search a citizen through Call Center Console verify his/her eligibility.
    Given user is on Login Page.
    When the user provide the "User Name" and "Password", and clicks the "Login" button, the user is navigated to the "Home" screen.
    Then the user search with citizen with his/her registration number and check if the record is there or not.
    And the clicks and opens the user record.
    Then the user clicks on the "Eligibility Crieteria" button, selects the "Vaccination" option and check if the patient is eligible.
