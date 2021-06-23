Feature: select player who goes first
    Scenario: To select the player who goes first
        Given user opens home page
        When the home page is loaded
        Then user should see two buttons along with related text

    Scenario: if Blue Hero goes first
        Given home page is displayed with two buttons
        When the user clicks on blue hero
        Then user should see four drop buttons enabled and nothing filled.

    Scenario: if Red CPU goes first
        Given home page is displayed with two buttons
        When the user clicks on Red CPU
        Then user should see four drop buttons enabled and one position is filled.