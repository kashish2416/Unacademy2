Feature: Setting Page
  Background: login to unacademy
    Given Chrome is opened and Unacademy app is opened
    When User clicks on login button
    When User enters Mobile Number "9373020586"
    And User again clicks on login button
    And User enters otp
    And User clicks on verify otp button

Scenario: Validate user is not able to modify information with Invalid data
      And User clicks on Profile button
      And User clicks on settings
      And User click on username field
      And User sends <invalid> data
      And Clicks on save button
      Then It shows result in page1
