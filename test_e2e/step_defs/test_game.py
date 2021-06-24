import pytest
from pytest_bdd import given, when, then, scenario
from test_e2e.helpers.select_player_helper import select_player


@scenario('../features/select_player.feature', 'To select the player who goes first', )
def test_scenario():
    pass


@given("user opens home page")
def test_given(driver):
    #driver.get("www.google.com")
    sp = select_player(driver)
    sp.click_blue_button()

@when("the home page is loaded")
def test_when():
    pass

@then("user should see two buttons along with related text")
def test_then():
    pass

#@pytest.mark.usefixtures("setUp")
#class Testgame(Baseclass):

 #   def test_game(self):
  #      message = self.driver.find_element_by_css_selector("button,id").text
  #      if message == "BLUE HERO":
  #         print("WOHOO")
# @pytest.mark.usefixtures("setUp")
# class Test_one():
#
#     def test_game(self):
#         self.driver.get("http://ninedt.herokuapp.com/#/game")
#         display_message = self.driver.find_element_by_xpath("//div[@ng-if='!game.boards || !game.boards.length']").text
#         assert display_message == 'Who goes first? BLUE HERO RED CPU'

