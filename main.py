from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()

# открытие страницы
driver.get("http://www.instagram.com")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# ввод имя и пароль
username.clear()
username.send_keys("Name")
password.clear()
password.send_keys("Password")

# target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

time.sleep(5)
alert = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Не сейчас")]'))).click()
alert2 = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Не сейчас")]'))).click()

# поле ввода для поиска
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Поиск']")))
searchbox.clear()

# поиск по хэштегу
keyword = "#space"
searchbox.send_keys(keyword)

time.sleep(8)  # ожидание 8 секунд
my_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + keyword[1:] + "/')]")))
my_link.click()

# скролл
n_scrolls = 3
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    anchors = driver.find_elements_by_tag_name('a')
    anchors = [a.get_attribute('href') for a in anchors]
    anchors = [a for a in anchors if str(a).startswith("https://www.instagram.com/p/")]

    print('Found ' + str(len(anchors)) + ' links to images')

images = []

# переход по ссылке и извлечение изображения с индексом 1
for a in anchors:
    driver.get(a)
    time.sleep(5)
    img = driver.find_elements_by_tag_name('img')
    img = [i.get_attribute('src') for i in img]
    images.append(img[1])

# Сохранение изображений на компьютер
import os
import wget

path = os.getcwd()
path = os.path.join(path, keyword[1:])

# Создание директории
os.mkdir(path)

path

# Загрузка изображений
counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
