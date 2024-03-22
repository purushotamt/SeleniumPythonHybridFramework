from selenium.webdriver.common.by import By

from pageobjectmodule.AccountPage import AccountPage
from pageobjectmodule.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        #self.driver = driver
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_address(self, email_address):
        self.type_into_element(email_address,"email_address_field_id",self.email_address_field_id)
        # self.driver.find_element(By.ID, self.email_address_field_id).click()
        # self.driver.find_element(By.ID, self.email_address_field_id).clear()
        # self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_address)

    def enter_password(self, password_text):
        self.type_into_element(password_text,"password_field_id", self.password_field_id)
        # self.driver.find_element(By.ID, self.password_field_id).click()
        # self.driver.find_element(By.ID, self.password_field_id).clear()
        # self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath",self.login_button_xpath)
        #self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return AccountPage(self.driver)

    def retrieve_warning_message(self):
        return self.retrieve_element_text("warning_message_xpath",self.warning_message_xpath)
        #return self.driver.find_element(By.XPATH, self.warning_message_xpath).text

    def login_to_application(self, email_address, password_text):
        self.enter_email_address(email_address)
        self.enter_password(password_text)
        return self.click_on_login_button() # this will return object of AccountPage
