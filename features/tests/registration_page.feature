# Created by HP at 3/10/2020
Feature: Verify that Registration flow works as expected

  Scenario: Verify that Registration flow works as expected
    Given Open https://www.gamestop.com/ page
    When Click account button
    And Switch to create account
    And Fill all fields with fake data
    Then Click submit
    And Expected registration will be complete successfully


  Scenario: Verify that Sign-In with existing account works
    Given Open https://www.gamestop.com/ page
    When Click account button
    And Fill data from prev step
    Then Click signIn
    And Expected login will be complete successful
