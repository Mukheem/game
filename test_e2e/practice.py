from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("http://ninedt.herokuapp.com/#/game")
message= driver.find_element_by_css_selector("button,id").text
if message == "BLUE HERO":
    drops = driver.find_element_by_css_selector("button[class*='btn btn-primary ng-scope']")
    for drop in drops():
        drop.click()
        break