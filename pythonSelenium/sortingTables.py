from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedveggies = []
service_obj = Service("C:/Users/sai/Desktop/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names  -  BrowserSortedVeggieList   (A,B,C)
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggieWebElements:
    browserSortedveggies.append(element.text)
originalBrowserSortedList = browserSortedveggies.copy()

# sort this BrowserSortedVeggieList ==>  newSortedList
browserSortedveggies.sort()

# BrowserSortedVeggieList == newSortedList
assert browserSortedveggies == originalBrowserSortedList