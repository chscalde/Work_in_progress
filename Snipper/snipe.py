from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


website = "https://computers.woot.com/offers/barkan-7-12-in-tablet-mount-3?ref=w_ngh_dd_cp"
email = "e-mail"
password = "pass"


driver = webdriver.Firefox()
driver.get(website)


driver.find_element_by_link_text("Add to cart").click()
time.sleep(.5)
driver.find_element_by_link_text("proceed to checkout").click()
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


print("Waiting....")
time.sleep(10)
driver.close()
