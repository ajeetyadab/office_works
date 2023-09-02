import os
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as e
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.service import Service
from selenium.webdriver.firefox.service import Service

from selenium.webdriver.chrome.options import Options
import time

# importing excel functions
from xutility import read_data

os.getcwd()

ser_ob = Service("./geckodriver.exe")
driver = webdriver.Firefox(service=ser_ob)
wait = WebDriverWait(driver,5)
driver.implicitly_wait(10)