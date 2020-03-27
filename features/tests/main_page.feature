# Created by HP at 3/7/2020
Feature: User is taken to the search results page

  Scenario: User is taken to the search results page
    Given Open https://www.gamestop.com/ page
    When Insert gaming mouse in search field
    And Click search button or click enter button
    Then Expect to see the search results page. Check that title is relevant to search text



  Scenario: Shopping cart - empty state
    Given Open https://www.gamestop.com/ page
    When Click cart button
    Then Expected cart page will have Empty in the title


  Scenario: User is able to write a review
    Given Open https://www.gamestop.com/ page
    When Insert keyboard in search field
    And On search results page choose something and click it
    Then expected product has "write review" button
    Then click "write review" button



    Scenario Outline: Verify that Auto-suggestion works
      Given Open https://www.gamestop.com/ page
      When Insert <keyword> in search field
      Examples:
        | keyword  |
        | FIFA 20  |
        | Pokemon  |
        | GTA 5    |
        | Keyboard |
      Then Wait a couple of seconds
      And Expected to see some suggestions. Count them










