from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.firefox.service import Service
import openpyxl
from xutility import read_data
from xutility import write_data
from selenium.webdriver.firefox.options import Options


#driver_path = "./chromedriver.exe"

ops=Options()
ops.headless=True 
ser_ob = Service(r"C:/Users/acer/Desktop/python codes/geckodriver.exe")
driver = webdriver.Firefox(service=ser_ob,options=ops)





DISTRICT_VALUE = "136"
TEHSHIL_VALUE = "00723"
FASAL_NAME_VALUE = "3"
SICAHAI_VIDHI = "6"

"""importing data from xl_sheet"""

file="C:/Users/acer/Desktop/auto_khasra.xlsx"
wb=openpyxl.load_workbook(file)
ws=wb["do_fasli"]
sheet=wb["Sheet2"]

xl_data1=read_data(file,"do_fasli",2,2)

xl_data_teen_fasli1=read_data(file,"do_fasli",3,2)


xl_data2=xl_data1.split(",")

xl_data_teenfasli_list=xl_data_teen_fasli1.split(",")


xl_data3_to_leave=[]

xl_data_teen_fasli2=[]

xl_data_total_gata1=read_data(file,"do_fasli",1,2)
xl_data_total_gata2=int(xl_data_total_gata1)
gata_start=read_data(file,"do_fasli",4,2)






"""looping to convert string to list"""
def string_to_list(data1,data2):
    for i in data1:
        data2.append(int(i))

string_to_list(xl_data2,xl_data3_to_leave)
string_to_list(xl_data_teenfasli_list,xl_data_teen_fasli2)

tehsil=read_data(file,"do_fasli",2,3)
password=read_data(file,"do_fasli",2,4)
print(type(password))

village1=read_data(file, "do_fasli", 3, 3)
fasal1=read_data(file,"do_fasli",2,5)



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
    driver.get("http://164.100.59.148/")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/center/main/div/div/ul/li[4]/a/div/div[1]").click()
    time.sleep(.25)


def load_second_page():
    selectDistrict = Select(driver.find_element(By.ID, "up_district"))
    selectDistrict.select_by_visible_text("रामपुर")
    time.sleep(.5)
    selectTehsil = Select(driver.find_element(By.ID, "up_tehsil"))
    selectTehsil.select_by_value(TEHSHIL_VALUE)
    time.sleep(1.5)
    selectTehsil = Select(driver.find_element(By.ID, "up_halka"))
    selectTehsil.select_by_visible_text(tehsil)
    time.sleep(.5)
    captcha_value = driver.find_element(By.ID, "CaptchaDiv").text
    driver.find_element(By.ID, "CaptchaInput").send_keys(captcha_value)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "login100-form-btn").click()


def load_third_page():
    time.sleep(2)
    village = Select(driver.find_element(By.ID, "gram_name"))
    village.select_by_visible_text(village1)
    time.sleep(.5)
    fasal_year = Select(driver.find_element(By.ID, "fasalYear"))
    fasal_year.select_by_visible_text("1429 (1 जुलाई 2021 से 30 जून 2022)")
    time.sleep(.5)
    fasal=Select(driver.find_element(By.ID,"fasal"))
    fasal.select_by_index(fasal1)
    time.sleep(1)
    alert_window=driver.switch_to.alert
    print(alert_window.text)
    alert_window.accept()
    time.sleep(.5)
    driver.find_element(By.CLASS_NAME, "login100-form-btn").click()


def load_fourth_page():
    time.sleep(2)
    alert_window = driver.switch_to.alert
    print(alert_window.text)
    alert_window.accept()
    time.sleep(.5)
    driver.find_element(By.ID,"link2").click()
    fill_form()


def fill_form():
    time.sleep(0.5)
    for i in range(gata_start,xl_data_total_gata2):
        if i in xl_data3_to_leave:
            print(i,"khali gaata")
            sheet.append([f"{i}","khali gata"])
            wb.save(file)


            continue
        if i in xl_data_teen_fasli2:
            fill_teen_khasra_pravisti(i)



        fill_khasra_pravisti(i)



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
        driver.find_element(By.XPATH, "//*[@id=\"tab-4\"]/form/p/table[2]/tbody/tr/td[1]/input[1]").click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, "//*[@id=\"content\"]/center/header/div/div[7]/div").click()
        sheet.append([f"{i}", "do fasali"])
        wb.save(file)
        print(i,"do fasli")


    except TimeoutException as e:
        driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
        time.sleep(3)


def fill_teen_khasra_pravisti(i):
    search_number(i)
    time.sleep(0.5)
    try:
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.NAME, "khata_number")))
        driver.find_element(By.NAME, "khata_number").click()
        driver.find_element(By.XPATH, "//*[@id=\"case_frm\"]/button[7]").click()
        time.sleep(1)
        gata_area_text = driver.find_element(By.XPATH, "//*[@id=\"tabs-container\"]/div[1]/label[3]").text
        gata_area = 2 * (float(gata_area_text.split(":")[1].strip()))
        driver.find_element(By.ID, "doFasliSichitArea").clear()
        driver.find_element(By.ID, "doFasliSichitArea").send_keys(gata_area)
        driver.find_element(By.XPATH, "//*[@id=\"tab-4\"]/form/p/table[2]/tbody/tr/td[1]/input[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id=\"content\"]/center/header/div/div[7]/div").click()
        print(i,"teen fasli")
        ws.append([f"{i}", "teen fasali"])
        wb.save(file)


    except TimeoutException as e:
        driver.find_element(By.XPATH, number_x_path_map["clear"]).click()
        time.sleep(3)


load_first_page()
load_second_page()
load_third_page()
load_fourth_page()


