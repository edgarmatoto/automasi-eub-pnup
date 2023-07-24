from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

driver = webdriver.Chrome()

driver.get("https://simponi.poliupg.ac.id:8080/index.php")

nim = ''
password = ''
jumlah_mata_kuliah = 7

driver.find_element(By.NAME, "txtEmail").clear()
driver.find_element(By.NAME, "txtEmail").send_keys(nim)

driver.find_element(By.NAME, "txtPassword").clear()
driver.find_element(By.NAME, "txtPassword").send_keys(password)

Login = driver.find_element(By.NAME, "Button")
Login.click()

akademik_navbar = WebDriverWait(driver, timeout=25).until(lambda d: d.find_element(By.LINK_TEXT, "Akademik"))
akademik_navbar.click()
driver.find_element(By.LINK_TEXT, "Evaluasi Umpan Balik (EUB)").click()

klik_disini = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.LINK_TEXT, "Klik disini untuk melanjutkan"))
klik_disini.click()

for i in range(1, jumlah_mata_kuliah + 1):
    mata_kuliah = WebDriverWait(driver, timeout=25).until(lambda d: d.find_element(By.ID, "cbMatakuliah"))
    mata_kuliah.click()

    list_mata_kuliah = mata_kuliah.find_elements(By.TAG_NAME, 'option')
    list_mata_kuliah[i].click()
        
    for j in range(1, 22):
        random_option = random.randint(1, 4)
        selected_option = WebDriverWait(driver, timeout=25).until(lambda d: d.find_element(By.ID, f"b{j}_{random_option}"))
        selected_option.click()
        
        suggestion = ['kurang baik', 'cukup baik', 'baik', 'cukup baik', 'sangat baik']

    for k in range(1, 3):
        random_suggestion_index = random.randint(0, len(suggestion) - 1)
        selected_suggestion = suggestion[random_suggestion_index]

        suggestion_element = driver.find_element(By.NAME, f"jawabanSaran{k}")
        suggestion_element.send_keys(selected_suggestion)

    submit_button_element = driver.find_element(By.ID, "Simpan")
    submit_button_element.click()

time.sleep(10)