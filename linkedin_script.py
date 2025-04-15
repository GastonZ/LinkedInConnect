import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv

import os

load_dotenv()

USERNAME = os.getenv("USERNAME")   
PASSWORD = os.getenv("PASSWORD")      
MAX_CONNECTIONS = 80                  

def login(driver):
    driver.get("https://www.linkedin.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("✅ Sesión iniciada correctamente")
    time.sleep(3)

def connect_from_mynetwork(driver):
    driver.get("https://www.linkedin.com/flagship-web/mynetwork/grow/")
    time.sleep(5)

    connections = 0
    scroll_attempts = 0
    max_scroll_attempts = 20
    last_height = driver.execute_script("return document.body.scrollHeight")

    while connections < MAX_CONNECTIONS and scroll_attempts < max_scroll_attempts:
        buttons = driver.find_elements(By.XPATH, "//span[text()='Conectar' or text()='Connect']/ancestor::button")

        if buttons:
            print(f"🔎 Encontrados {len(buttons)} botones de conexión")
            for button in buttons:
                if connections >= MAX_CONNECTIONS:
                    break
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", button)
                    time.sleep(0.5)
                    driver.execute_script("arguments[0].click();", button)
                    print(f"[+] Conexión enviada ({connections + 1})")
                    connections += 1
                    time.sleep(2)
                except Exception as e:
                    print("[-] No se pudo hacer clic en un botón:", e)
                    continue
        else:
            print(f"⚠️ No se encontraron botones. Scroll #{scroll_attempts + 1}")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            scroll_attempts += 1
        else:
            scroll_attempts = 0 
            last_height = new_height




def main():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = uc.Chrome(options=options)

    try:
        login(driver)
        connect_from_mynetwork(driver)
    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    main()
