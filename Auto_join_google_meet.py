# Written By Ashish Mishra, version 1.0
# As google won't let you login from an automated script so used stackoverflow insted of Google
# Only dependency needed is selenium (pip install selenium) and 
# chromedriver(As I used Chrome browser for this download it from https://chromedriver.chromium.org/ 
# extract the zip from above link and paste the path at line 14 executable_path = " path " like  C:\Drivers\chromedriver.exe
# Thats it you are ready to rock

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="Chrome_driver_path")
driver.implicitly_wait(5)
meet_link ="Meeting link"
driver.get("https://stackoverflow.com/users/login")

driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()

wait=WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"identifierId\"]"))).send_keys("Your Gmail")
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"password\"]/div[1]/div/div[1]/input"))).send_keys("Your Password")
driver.find_element_by_xpath("//*[@id=\"passwordNext\"]/div/button/div[2]").click()
time.sleep(10) # important it takes time to load Stackoverflow so adjust according to your internet speed 

driver.get(meet_link)
wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"yDmH0d\"]/div[3]/div/div[2]/div[3]/div/span/span"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id=\"yDmH0d\"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span"))).click()
