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
    pin = config.get('pin')
    time_between_reloads = int(config.get('time_between_reloads'))
    url = "https://candidates.ibo.org/#/Login"
except:
    print("Invalid config.txt")
    exit()

while True:
    driver = webdriver.Chrome()
    driver.get(url)

    driver.find_element(By.ID, "personCode").send_keys(personal_code)
    driver.find_element(By.ID, "pinCode").send_keys(pin)
    print("Entered login data successfully")

    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ibo-btn-primary.login.mt-40")))
    login_button.click()
    print("Logged in successfully")

    navigation_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ibo-btn-primary.mt-4")))
    navigation_button.click()
    print("Navigated to results successfully")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    print("Page has finished loading")

    time.sleep(time_between_reloads)
    driver.quit()
