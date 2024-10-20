Feature: User Login

  Scenario: Successful Login
    Given the user accesses the login page
    When the user enters the credentials "standard_user" and "secret_sauce"
    And clicks on the login button
    Then the user should be redirected to the home page

  Scenario Outline: Unsuccessful Login Attempts
    Given the user accesses the login page
    When the user enters the credentials "<username>" and "<password>"
    And clicks on the login button
    Then the user should remain on the login page
    And an error message should be displayed

    Examples:
      | username      | password       |
      | wrong_user    | secret_sauce   |
      | standard_user | wrong_password |
      | wrong_user    | wrong_password |
