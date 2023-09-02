from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

driver_path = "./chromedriver.exe"
driver = webdriver.Chrome(driver_path)
PASSWORD = "Anil@151"
DISTRICT_VALUE = "136"
TEHSHIL_VALUE = "00727"
HALKA_VALUE = "0113600727030"
FASAL_NAME_VALUE = "3"
SICAHAI_VIDHI = "6"

number_x_path_map = {
    "1": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[1]/a/div",
    "2": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[2]/a/div",
    "3": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[3]/a/div",
    "4": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[1]/td[4]/a/div",
    "5": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[1]/a/div",
    "6": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[2]/a/div",
    "7": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[3]/a/div",
    "8": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[2]/td[4]/a/div",
    "9": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[1]/a/div",
    "0": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[2]/a/div",
    "delete": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[3]/a/div",
    "clear": "//*[@id=\"searchGata\"]/div/div[3]/table/tbody/tr[3]/td[4]/a/div"
}


def load_first_page():
    driver.get("http://164.100.59.148/homePage_login_khasra.jsp")
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/center/main/div/div/ul/li[4]/a/div/div[1]").click()
    time.sleep(.25)


def load_second_page():
    selectDistrict = Select(driver.find_element(By.ID, "up_district"))
    selectDistrict.select_by_visible_text("रामपुर")
    time.sleep(.5)
    selectTehsil = Select(driver.find_element(By.ID, "up_tehsil"))
    selectTehsil.select_by_value(TEHSHIL_VALUE)
    time.sleep(.5)
    selectTehsil = Select(driver.find_element(By.ID, "up_halka"))
    selectTehsil.select_by_value(HALKA_VALUE)
    time.sleep(.5)
    captcha_value = driver.find_element(By.ID, "CaptchaDiv").text
    driver.find_element(By.ID, "CaptchaInput").send_keys(captcha_value)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.CLASS_NAME, "login100-form-btn").click()


def load_third_page():
    time.sleep(20)
    # driver.find_element(By.CLASS_NAME, "login100-form-btn").click()


def load_fourth_page():
    time.sleep(10)
    # driver.find_element(By.XPATH, "//*[@id=\"link2\"]/a/div/div[2]").click()
    fill_form()


def fill_form():
    time.sleep(0.5)
    for i in range(274,300):
        # Add custom range here for alternate entry
        if i in [37,39,40,78,80,81,85,89,90,91,98,105,106,107,108,109,136,137,144,145,151,202,203,204,212,213,220,221,224,225,226,229,232,238,246,247,250,251,254,273,274,281,289,290]:
            print(i)
            # alternate_entry(i)
            continue
        fill_khasra_pravisti(i)
        print(i)


def click_digits(digits):
    for digit in digits:
        driver.find_element(By.XPATH, number_x_path_map[digit]).click()


def search_number(number):
    click_digits(str(number))
    driver.find_element(By.XPATH, "//*[@id=\"sgw\"]/button/i").click()


def fill_final_page():
    Select(driver.find_element(By.ID, "fasal_name")).select_by_value("56")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"tab-3\"]/form/p/table[3]/tbody/tr/td[1]/input[5]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id=\"content\"]/center/header/div/div[7]/div").click()


def alternate_entry(i):
    search_number(i)
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "khata_number")))
        driver.find_element(By.NAME, "khata_number").click()
        driver.find_element(By.XPATH, "//*[@id=\"case_frm\"]/button[2]").click()
        Select(driver.find_element(By.ID, "fasal_name")).select_by_value(FASAL_NAME_VALUE)
        time.sleep(1)
        agri_area = driver.find_element(By.ID, "agriArea").get_attribute('value')
        Select(driver.find_element(By.ID, "agriTech")).select_by_value(SICAHAI_VIDHI)
        driver.find_element(By.ID, "sichitArea").clear()
        driver.find_element(By.ID, "sichitArea").send_keys(agri_area)
        driver.find_element(By.XPATH, "//*[@id=\"tab-3\"]/form/p/table[3]/tbody/tr/td[1]/input[5]").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//*[@id=\"content\"]/center/header/div/div[7]/div").click()
        time.sleep(0.5)
    except TimeoutException as e:
        driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
        time.sleep(3)


def fill_khasra_pravisti(i):
    search_number(i)
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "khata_number")))
        driver.find_element(By.NAME, "khata_number").click()
        driver.find_element(By.XPATH, "//*[@id=\"case_frm\"]/button[7]").click()
        time.sleep(1)
        gata_area_text = driver.find_element(By.XPATH, "//*[@id=\"tabs-container\"]/div[1]/label[3]").text
        gata_area = float(gata_area_text.split(":")[1].strip())
        driver.find_element(By.ID, "doFasliSichitArea").clear()
        driver.find_element(By.ID, "doFasliSichitArea").send_keys(gata_area)
        driver.find_element(By.XPATH,"//*[@id=\"tab-4\"]/form/p/table[2]/tbody/tr/td[1]/input[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id=\"content\"]/center/header/div/div[7]/div").click()


    except TimeoutException as e:
        driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
        time.sleep(3)


load_first_page()
load_second_page()
load_third_page()
load_fourth_page()
