from pytest_bdd import given, when, then, scenario


@scenario('../features/select_player.feature', 'To select the player who goes first')
def test_scenario():
    pass



@given("user opens home page")
def test_given():
    pass

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


