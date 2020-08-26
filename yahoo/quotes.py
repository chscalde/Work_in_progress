from selenium import webdriver
from selenium.webdriver.common.keys import Keys


ticker = "AAPL"

driver = webdriver.Firefox()
driver.get("https://finance.yahoo.com/quote/" + ticker)
element = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[4]/div/div/div")

print(element)
driver.close()
