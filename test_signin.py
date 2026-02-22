from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from datatools import TestData
from datatools import Gender
import unittest


class RegisterNewUserTest(unittest.TestCase):
    def setUp(self):
        # preconditions
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationpractice.techwithjatin.com/")

    @unittest.skip("skipping test_no_name_in_registration_form")
    def test_no_name_in_registration_form(self):
        # test steps
        #fill in and click Create an account form
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()
        self.driver.find_element(By.ID, "email_create").send_keys(TestData.EMAIL)
        self.driver.find_element(By.ID, "SubmitCreate").click()

        #select gender checkbox
        if TestData.GENDER == Gender.FEMALE:
            gender_female = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="id_gender2"]')))
            gender_female.click()
        else:
            gender_male = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//label[@for="id_gender1"]')))
            gender_male.click()
        # self.driver.implicitly_wait(3)

        #fill in last name
        self.driver.find_element(By.ID, "customer_lastname").send_keys(TestData.LAST_NAME)

        #verify email
        email_input = self.driver.find_element(By.ID, "email")
        email_actual = email_input.get_attribute("value")
        self.assertEqual(TestData.EMAIL, email_actual)

        #enter password
        self.driver.find_element(By.ID, "passwd").send_keys(TestData.VALID_PASSWORD)

        # select date of birth
        day = Select(self.driver.find_element(By.ID, "days"))
        day.select_by_value(TestData.BRITH_DAY)
        month = Select(self.driver.find_element(By.ID, "months"))
        month.select_by_value(TestData.BRITH_MONTH)
        year = Select(self.driver.find_element(By.ID, "years"))
        year.select_by_value(TestData.BRITH_YEAR)

        #click register
        self.driver.find_element(By.ID, "submitAccount").click()
        self.driver.implicitly_wait(2)

        #assert - verify nr of alerts
        error_message = self.driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p[1]')
        self.assertEqual("There is 1 error", error_message.text)
        print(error_message.text)
        error_list = self.driver.find_elements(By.XPATH, '//div[@class="alert alert-danger"]/ol/li')
        self.assertEqual(1, len(error_list))

        #assert - verify of error message
        self.assertEqual("firstname is required.", error_list[0].text)
        sleep(3)

    def test_password_too_short(self):
        # test steps
        # fill in and click Create an account form
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in").click()
        self.driver.find_element(By.ID, "email_create").send_keys(TestData.EMAIL)
        self.driver.find_element(By.ID, "SubmitCreate").click()

        # select gender checkbox
        if TestData.GENDER == Gender.FEMALE:
            gender_female = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="id_gender2"]')))
            gender_female.click()
        else:
            gender_male = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//label[@for="id_gender1"]')))
            gender_male.click()
        # self.driver.implicitly_wait(3)

        #fill in first name
        self.driver.find_element(By.ID, "customer_firstname").send_keys(TestData.FIRST_NAME)

        # fill in last name
        self.driver.find_element(By.ID, "customer_lastname").send_keys(TestData.LAST_NAME)

        # verify email
        email_input = self.driver.find_element(By.ID, "email")
        email_actual = email_input.get_attribute("value")
        self.assertEqual(TestData.EMAIL, email_actual)

        # enter password
        self.driver.find_element(By.ID, "passwd").send_keys(TestData.INVALID_PASSWORD)

        # select date of birth
        day = Select(self.driver.find_element(By.ID, "days"))
        day.select_by_value(TestData.BRITH_DAY)
        month = Select(self.driver.find_element(By.ID, "months"))
        month.select_by_value(TestData.BRITH_MONTH)
        year = Select(self.driver.find_element(By.ID, "years"))
        year.select_by_value(TestData.BRITH_YEAR)

        # click register
        self.driver.find_element(By.ID, "submitAccount").click()
        self.driver.implicitly_wait(2)

        # assert - verify nr of alerts
        error_message = self.driver.find_element(By.XPATH, '//div[@class="alert alert-danger"]/p[1]')
        self.assertEqual("There is 1 error", error_message.text)
        print(error_message.text)
        error_list = self.driver.find_elements(By.XPATH, '//div[@class="alert alert-danger"]/ol/li')
        self.assertEqual(1, len(error_list))

        # assert - verify of error message
        self.assertEqual("passwd is invalid.", error_list[0].text)
        sleep(3)

    def tearDown(self):
        self.driver.quit()