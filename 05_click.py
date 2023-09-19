# https://youtu.be/Ice4M4NqKgE?list=PLbFzTYWXNlJ4BrHcQ5dVhy9xhLtLg2Kcr

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

service = Service("./drivers/msedgedriver.exe")
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(service=service, options=options)
driver.maximize_window()
driver.get("https://duckduckgo.com/")
search_box = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Search with DuckDuckGo"]') # selects element by CSS selector
search_box.send_keys("hello") # prints text to the selected html element
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Search"]').click() # Click on the selected html element but if it cover or overlapped with sth, it can not be clicked
driver.find_element(By.ID, "r1-0").click()






