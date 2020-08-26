from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


website = ""  # Add login website here
email = "e-mail"
password = "pass"


driver = webdriver.Firefox()
driver.add_cookie({"name": "key", "value": "value"})
driver.get(website)

for i in range(10):
    print(i)
    try:
        driver.find_element_by_name("rememberMe").click()
        driver.find_element_by_id("signInExpandButton").click()
        break
    except NoSuchElementException:
        time.sleep(.5)
        print("fudge me")
emailbox = driver.find_element_by_name("email")
emailbox.send_keys(email)
passbox = driver.find_element_by_name("password")
passbox.send_keys(password)
driver.find_element_by_id("signInSubmit").click()
