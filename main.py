from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.by import By

class Gender:
    MALE = 0
    FEMALE = 1

#test data
DATA_EMAIL = "janedoe@sample.sample"
DATA_GENDER = Gender.MALE

driver = Chrome()
# open landing page
driver.get("https://automationpractice.techwithjatin.com/")
sleep(3)

# maximize window
driver.maximize_window()

#find element
sign_in_a = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
sign_in_a.click()

#click email input
driver.find_element(By.ID, "email_create").send_keys(DATA_EMAIL)

#click create account button
driver.find_element(By.ID, "SubmitCreate").click()

driver.implicitly_wait(5)
#select gender
if DATA_GENDER == Gender.FEMALE:
    driver.find_element(By.XPATH, '//label[@for="id_gender2"]').click()
else:
    driver.find_element(By.XPATH, '//label[@for="id_gender1"]').click()

print(type(sign_in_a))
sleep(5)
driver.quit()