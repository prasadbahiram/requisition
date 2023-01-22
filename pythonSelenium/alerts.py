import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/sai/Desktop/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Prasad")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
time.sleep(2)
alerts = driver.switch_to.alert
alertsText = alerts.text
print(alertsText)
assert "Prasad" in alertsText
alerts.accept()
#alerts.dismiss()



