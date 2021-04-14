Feature: Vaccine Registration

  @reg_thru_portal
  Scenario: Register a citizen through portal.
    Given user is on Citizen portal HOME page
    When the user clicks "Register" button, the user is navigated to a 3 step form screen.
    Then the user fills the personal details and click "Continue" button.
    And the user enters the "email" or "sms phone number" to send confirmation and click "Continue" button.
    Then the user verify all the detail provided, hit "consent" button and clicks "Submit" button to submit the registration successfully.
    And the user copies "registration confirmation number" and save it.
