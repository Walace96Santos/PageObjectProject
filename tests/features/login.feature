Feature: User Login

  Scenario: Successful Login
    Given the user accesses the login page
    When the user provides valid credentials
    And clicks on the login button
    Then the user should be redirected to the home page