# https://youtu.be/hwD2mDkMfN8?list=PLbFzTYWXNlJ4BrHcQ5dVhy9xhLtLg2Kcr

from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service("./drivers/msedgedriver.exe")
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(service=service, options=options)

driver.get("https://www.apple.com/") 
link = driver.current_url  
title = driver.title  
print("the title of the page is: " + title)
if "apple.com" in link:
    print("you are on the right Apple page: " + link)

driver.maximize_window()

driver.get("https://www.etsy.com/")
link = driver.current_url
title = driver.title
print("the title of the page is: " + title)
if "etsy.com" in link:
    print("you are on the right ETSY page: " + link)

driver.back()
title = driver.title
if "Applesssssss" in title:
    print("Congratulations, you returned to the apple page: " + title)
else:
    driver.save_screenshot("./screenshots/screenshot1.png")

driver.quit() 
