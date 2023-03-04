Feature: Setting Page
  Background: login to unacademy
    Given Chrome is opened and Unacademy app is opened
    When User clicks on login button
    When User enters Mobile Number "9373020586"
    And User again clicks on login button
    And User enters otp
    And User clicks on verify otp button


  Scenario: Validate user login and navigates on to Settings page
    And User clicks on Profile button
    And User clicks on settings
    Then It shows settings page

  Scenario: Validate State field functionality on settings page
    And User clicks on Profile button
    And User clicks on settings
    And User clicks on edit state button
    And Clicks on save button
    Then It shows updated state

  Scenario: Validate refresh functionality on settings page
    And User clicks on Profile button
    And User clicks on settings
    And User clicks on refresh button
    Then The page gets refreshed and user remains on same page

   Scenario: Validate user is able to modify information with valid data
      And User clicks on Profile button
      And User clicks on settings
      And User click on username field
      And User enters "kash"
      And Clicks on save button
      Then It shows updated username

 Scenario Outline: Validate user is not able to modify information with Invalid data
      And User clicks on Profile button
      And User clicks on settings
      And User click on username field
      And User enters <invalidusername>
      And Clicks on save button
      Then username is not updated
      Examples:
         |invalidusername|
         |@#%$           |
         |0000           |




