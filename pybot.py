from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()

browser.get('https://www.instagram.com')
browser.implicitly_wait(5)

actions = ActionChains

sleep(2)

username_input = browser.find_element(By.CSS_SELECTOR, "input[name='username']")
password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")

username_input.send_keys("test")
password_input.send_keys("test")

# actions.send_keys(Keys.RETURN)
# actions.perform()

ogin_link = browser.find_element(By.XPATH, "//button[contains(., 'Log in')]").send_keys(Keys.RETURN)
# login_link.click()

sleep(5)

# browser.close()