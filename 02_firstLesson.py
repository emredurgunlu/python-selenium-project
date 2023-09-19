""" from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./drivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service,options=options)
driver.get("https://www.apple.com/") """

# https://youtu.be/NKUQ4xWvcr0?list=PLbFzTYWXNlJ4BrHcQ5dVhy9xhLtLg2Kcr

from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service("./drivers/msedgedriver.exe")
options = webdriver.EdgeOptions()
# It keeps the site open, otherwise the site will close as soon as it is opened.
options.add_experimental_option("detach", True)
driver = webdriver.Edge(service=service, options=options)

driver.get("https://www.apple.com/")  # Where to go
link = driver.current_url  # Get the URL of the currently open website
title = driver.title  # Get the title of the currently open website
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
driver.refresh()
driver.forward()

driver.close() # closes the current window

driver.quit() # closes all windows used by selenium
