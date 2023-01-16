from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("C:/Users/003TCS744/Desktop/Selenium_Course/chromedriver/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()
Phones=driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for i in Phones:
    name=i.find_element(By.XPATH,"div/h4/a").text
    if name=='iphone X':
        i.find_element(By.XPATH,"div/button").click()
    break
driver.find_element(By.XPATH,"//div[@id='navbarResponsive']/ul/li/a").click()
#Check=driver.find_element(By.XPATH,"//div[@class='media']/div/h4/a").text
#if Check=='Blackberry':
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

driver.find_element(By.ID,"country").send_keys("ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
success=driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(success)


