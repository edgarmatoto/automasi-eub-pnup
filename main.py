from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get("https://simponi.poliupg.ac.id:8080/mQuiz_intro_teori.php")
driver.add_cookie({"name": "PHPSESSID", "value": "h9sekfb3ktf2aumd0kq9ldlph5"})

Login = driver.find_element(By.LINK_TEXT, "Login")
Login.click()

driver.find_element(By.LINK_TEXT, "Akademik").click()
driver.find_element(By.LINK_TEXT, "Evaluasi Umpan Balik (EUB)").click()

klik_disini = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.LINK_TEXT, "Klik disini untuk melanjutkan"))
klik_disini.click()

daftar_matakuliah = WebDriverWait(driver, timeout=25).until(lambda d: d.find_element(By.ID, "cbMatakuliah"))
daftar_matakuliah.click()

options = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.TAG_NAME, "option"))
print(options.text)

mata_kuliah = [
    'Bahasa Inggris Teknik',
    'Komunikasi Data',
    'Kesehatan dan Keselamatan Kerja',
    'Struktur Data',
    'Basis Data',
    'Pengukuran dan Instrumentasi',
    'Jaringan Komputer',
]

# for mk in mata_kuliah:
#     daftar_matakuliah = WebDriverWait(driver, timeout=15).until(lambda d: d.find_element(By.ID, "cbMatakuliah"))
#     daftar_matakuliah.click()
    
#     for option in range(0, 21):
        

time.sleep(5)