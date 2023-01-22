from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/sai/Desktop/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Locaters : ID, Name, ClassName, Linktext, Xpath, CSSSelector,  (#Id, .class  --> CSS)

# For Xpath -->  //tagname[@attribute='value'] -->  //input[@type='submit']
# FOr CSS -->  tagname[attribute='value'] -->  input[name='name']

driver.find_element(By.NAME, "email").send_keys("vaishu@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys('6677')
driver.find_element(By.ID, "exampleCheck1").click()

# Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
#dropdown.select_by_value()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.NAME, "name").send_keys("Vaishali")
message = driver.find_element(By.CLASS_NAME, "alert ").text
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio2']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("prasad")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
print(message)
assert 'Success' in message





