from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotSelectableException,ElementNotVisibleException,ElementNotVisibleException,NoSuchElementException
import time

driver_path = "./chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
check_list=driver.find_elements(By.XPATH,"//*[@class='form-check-input' and contains(@id,'day')]")
for i in range(0,len(check_list)):
    print(i)
    if i<=1:
        check_list[i].click()
    
    