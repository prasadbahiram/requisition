from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/sai/Desktop/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break


radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
#radiobuttons[2].click()
#assert radiobuttons[2].is_selected()
for radio in radiobuttons:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        assert radio.is_selected()
        break

# Displayed
assert driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.XPATH, "//input[@id='displayed-text']").is_displayed()


