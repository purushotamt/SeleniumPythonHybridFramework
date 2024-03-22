from selenium.webdriver.common.by import By

from pageobjectmodule.BasePage import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self, driver):
        #self.driver = driver
        super().__init__(driver)

    account_creation_message_xpath = "//div[@id='content']/h1"

    def retrieve_account_creation_message(self):
        return self.retrieve_element_text("account_creation_message_xpath",self.account_creation_message_xpath)
        #return self.driver.find_element(By.XPATH, self.account_creation_message_xpath).text
