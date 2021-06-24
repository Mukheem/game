from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("http://ninedt.herokuapp.com/#/game")
display_message = driver.find_element_by_xpath("//div[contains(text(),'Who goes first?')]").is_displayed()
print(display_message)