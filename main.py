from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
# open landing page
driver.get("https://www.kozminski.edu.pl/pl")
sleep(5)
# maximize window
driver.maximize_window()
driver.switch_to_alert()
element.click("")
driver.quit()