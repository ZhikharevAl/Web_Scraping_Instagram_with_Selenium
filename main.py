from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome()

#open the webpage
driver.get("http://www.instagram.com")

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("waltafunk")
password.clear()
password.send_keys("Nulla1Rosa88")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


time.sleep(5)
alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Не сейчас")]'))).click()
alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Не сейчас")]'))).click()

# target the search input field
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Поиск']")))
searchbox.clear()

# search for the hashtag
keyword = "#space"
searchbox.send_keys(keyword)

# FIXING THE DOUBLE ENTER
time.sleep(5)  # Wait for 5 seconds
my_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()