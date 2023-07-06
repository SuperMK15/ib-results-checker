import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def read_config_file(file_path):
    config_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split(':')
                config_data[key.strip()] = value.strip()
    return config_data


try:
    file_path = 'config.txt'
    config = read_config_file(file_path)
    personal_code = config.get('personal_code')
    time_between_reloads = config.get('time_between_reloads')
    pin = config.get('pin')
    url = "https://candidates.ibo.org/#/Login"
except:
    print("Invalid config.txt")
    exit()

while True:
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, time_between_reloads)
    driver.get(url)

    try:
        personCodeForm = wait.until(EC.presence_of_element_located((By.ID, "personCode")))
        pinCodeForm = wait.until(EC.presence_of_element_located((By.ID, "pinCode")))
        print("Login page has finished loading")
        personCodeForm.send_keys(personal_code)
        pinCodeForm.send_keys(pin)
        print("Entered login data successfully")
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ibo-btn-primary.login.mt-40")))
        login_button.click()
        print("Logged in successfully")
    except:
        print("Login page was too slow to load... Retrying from the start")
        driver.quit()
        continue

    try:
        results_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ibo-btn-primary.mt-4")))
        results_button.click()
        print("Navigated to results successfully")
    except:
        print("Results button was too slow to load... Retrying from the start")
        driver.quit()
        continue

    try:
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Results page has finished loading")
        break
    except:
        print("Results page was too slow to load... Retrying from the start")
        driver.quit()
        continue

time.sleep(9999)
driver.quit()