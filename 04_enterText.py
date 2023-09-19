# https://youtu.be/cZRI5IjtD7w?list=PLbFzTYWXNlJ4BrHcQ5dVhy9xhLtLg2Kcr

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

service = Service("./drivers/msedgedriver.exe")
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()
driver.get("https://www.google.com/")
search_box = driver.find_element(By.ID, "APjFqb") # selects element by id
search_box.send_keys("hello") # prints text to the selected html element
search_box.send_keys(Keys.ENTER) # press Enter

# aramakutusu = driver.find_element(By.NAME, "search")
# aramakutusu.send_keys("Ay")
# print("bekleme basladi")
# time.sleep(1.0)
# print("bekleme bitti")
# # aramakutusu.send_keys(Keys.ENTER)
# # driver.find_element(By.XPATH, "//form[@id='searchform']//*[contains(text(), 'Ara')]").click()
# driver.find_element(By.CSS_SELECTOR, "form#searchform button").click()
# birinci_baslik = driver.find_element(By.ID, "firstHeading").text
# print("Ilk Baslik: " + birinci_baslik)
# driver.find_element(By.XPATH, "//a[text()='Dünya']").click()
# ikinci_baslik = driver.find_element(By.ID, "firstHeading").text
# print("Ikinci baslik: "+ikinci_baslik)




