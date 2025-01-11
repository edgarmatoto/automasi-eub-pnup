import time
import random
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://simponi.poliupg.ac.id:8080/index.php")

# Masukkan NIM dan PASSSWORD akun Simponi di dalam tanda petik dibawah
NIM = "42522011" 
PASSWORD = "Kontolusjr123*"

driver.find_element(By.NAME, "txtEmail").clear()
driver.find_element(By.NAME, "txtEmail").send_keys(NIM)

driver.find_element(By.NAME, "txtPassword").clear()
driver.find_element(By.NAME, "txtPassword").send_keys(PASSWORD)

Login = driver.find_element(By.NAME, "Button")
Login.click()

akademik_navbar = WebDriverWait(driver, timeout=25).until(lambda d: d.find_element(By.LINK_TEXT, "Akademik"))
akademik_navbar.click()
driver.find_element(By.LINK_TEXT, "Evaluasi Umpan Balik (EUB)").click()

klik_disini = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.LINK_TEXT, "Klik disini untuk melanjutkan"))
klik_disini.click()

select_element = WebDriverWait(driver, timeout=25).until(lambda d: d.find_element(By.ID, "cbMatakuliah"))
select = Select(select_element)
jumlah_mata_kuliah = len(select.options)

for i in range(1, jumlah_mata_kuliah + 1):
    try:
        select_element = WebDriverWait(driver, timeout=25).until(lambda d: d.find_element(By.ID, "cbMatakuliah"))
        select = Select(select_element)
        mata_kuliah = select.select_by_index(i)
            
        for j in range(1, 22):
            random_option = random.randint(2, 4)
            selected_option = WebDriverWait(driver, timeout=25).until(lambda d: d.find_element(By.ID, f"b{j}_{random_option}"))
            selected_option.click() 
        
        suggestion = ['cukup baik', 'baik', 'sangat baik']
        for k in range(1, 3):
            random_suggestion_index = random.randint(0, len(suggestion) - 1)
            selected_suggestion = suggestion[random_suggestion_index]

            suggestion_element = driver.find_element(By.NAME, f"jawabanSaran{k}")
            suggestion_element.send_keys(selected_suggestion)

        submit_button_element = driver.find_element(By.ID, "Simpan")

        submit_button_element.click()
    except:
        continue

time.sleep(10)