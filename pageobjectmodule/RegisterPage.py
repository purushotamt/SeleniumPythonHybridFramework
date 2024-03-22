from selenium.webdriver.common.by import By

from pageobjectmodule.AccountSuccesspage import AccountSuccessPage
from pageobjectmodule.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        #self.driver = driver
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//input[@value='1'][@name='newsletter']"
    duplicate_warning_message_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name_text):
        self.type_into_element(first_name_text,"first_name_field_id",self.first_name_field_id)
        # self.driver.find_element(By.ID, self.first_name_field_id).click()
        # self.driver.find_element(By.ID, self.first_name_field_id).clear()
        #
        # self.driver.find_element(By.ID, self.first_name_field_id).send_keys(first_name_text)

    def enter_last_name(self, last_name_text):
        self.type_into_element(last_name_text, "last_name_field_id",self.last_name_field_id)
        # self.driver.find_element(By.ID, self.last_name_field_id).click()
        # self.driver.find_element(By.ID, self.last_name_field_id).clear()
        #
        # self.driver.find_element(By.ID, self.last_name_field_id).send_keys(last_name_text)

    def enter_email(self, email_text):
        self.type_into_element(email_text,"self.email_field_id", self.email_field_id)
        # self.driver.find_element(By.ID, self.email_field_id).click()
        # self.driver.find_element(By.ID, self.email_field_id).clear()
        #
        # self.driver.find_element(By.ID, self.email_field_id).send_keys(email_text)

    def enter_telephone(self, telephone_text):
        self.type_into_element(telephone_text, "telephone_field_id",self.telephone_field_id)
        # self.driver.find_element(By.ID, self.telephone_field_id).click()
        # self.driver.find_element(By.ID, self.telephone_field_id).clear()
        #
        # self.driver.find_element(By.ID, self.telephone_field_id).send_keys(telephone_text)

    def enter_password(self, password_text):
        self.type_into_element(password_text,"password_field_id", self.password_field_id)
        # self.driver.find_element(By.ID, self.password_field_id).click()
        # self.driver.find_element(By.ID, self.password_field_id).clear()
        #
        # self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def enter_confirm_password(self, confirm_password_text):
        self.type_into_element(confirm_password_text,"confirm_password_field_id", self.confirm_password_field_id)
        # self.driver.find_element(By.ID, self.confirm_password_field_id).click()
        # self.driver.find_element(By.ID, self.confirm_password_field_id).clear()
        #
        # self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(confirm_password_text)

    def select_agree_checkbox_field(self):
        self.click_on_element("agree_field_name",self.agree_field_name)
        #self.driver.find_element(By.NAME, self.agree_field_name).click()

    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath",self.continue_button_xpath)
        #self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def select_yes_radio_button(self):
        self.click_on_element("yes_radio_button_xpath",self.yes_radio_button_xpath)
        #self.driver.find_element(By.XPATH, self.yes_radio_button_xpath).click()

    def retrieve_duplicate_email_warning(self):
        return self.retrieve_element_text("duplicate_warning_message_xpath",self.duplicate_warning_message_xpath)
        #return self.driver.find_element(By.XPATH, self.duplicate_warning_message_xpath).text

    def retrieve_privacy_policy_warning(self):
        return self.retrieve_element_text("privacy_policy_warning_xpath",self.privacy_policy_warning_xpath)
        #return self.driver.find_element(By.XPATH, self.privacy_policy_warning_xpath).text

    def retrieve_first_name_warning(self):
        return self.retrieve_element_text("first_name_warning_xpath",self.first_name_warning_xpath)
        #return self.driver.find_element(By.XPATH, self.first_name_warning_xpath).text

    def retrieve_last_name_warning(self):
        return self.retrieve_element_text("last_name_warning_xpath",self.last_name_warning_xpath)
        #return self.driver.find_element(By.XPATH, self.last_name_warning_xpath).text

    def retrieve_email_warning(self):
        return self.retrieve_element_text("email_warning_xpath",self.email_warning_xpath)
        #return self.driver.find_element(By.XPATH, self.email_warning_xpath).text

    def retrieve_telephone_warning(self):
        return self.retrieve_element_text("telephone_warning_xpath",self.telephone_warning_xpath)
        #return self.driver.find_element(By.XPATH, self.telephone_warning_xpath).text

    def retrieve_password_warning(self):
        return self.retrieve_element_text("password_warning_xpath",self.password_warning_xpath)
        #return self.driver.find_element(By.XPATH, self.password_warning_xpath).text

    def register_an_account(self, first_name_text, last_name_text, email_text, telephone_text, password_text,
                            confirm_password_text, yes_or_no, privacy_policy):
        self.enter_first_name(first_name_text)
        self.enter_last_name(last_name_text)
        self.enter_email(email_text)
        self.enter_telephone(telephone_text)
        self.enter_password(password_text)
        self.enter_confirm_password(confirm_password_text)
        if yes_or_no.__eq__("Yes"):
            self.select_yes_radio_button()
        if privacy_policy.__eq__("select"):
            self.select_agree_checkbox_field()
        return self.click_on_continue_button()

    def verify_all_warnings(self, expected_privacy_policy_warning, expected_first_name_warning_message,
                            expected_last_name_warning_message, expected_email_warning_message,
                            expected_telephone_warning_message, expected_password_warning_message):
        actual_privacy_policy_warning = self.retrieve_privacy_policy_warning()
        actual_first_name_warning_message = self.retrieve_first_name_warning()
        actual_last_name_warning_message = self.retrieve_last_name_warning()
        actual_email_warning_message = self.retrieve_email_warning()
        actual_telephone_warning_message = self.retrieve_telephone_warning()
        actual_password_warning_message = self.retrieve_password_warning()

        status = False
        if expected_privacy_policy_warning.__contains__(actual_privacy_policy_warning):
            if expected_first_name_warning_message.__contains__(actual_first_name_warning_message):
                if expected_last_name_warning_message.__contains__(actual_last_name_warning_message):
                    if expected_email_warning_message.__contains__(actual_email_warning_message):
                        if expected_telephone_warning_message.__contains__(actual_telephone_warning_message):
                            if expected_password_warning_message.__contains__(actual_password_warning_message):
                                status = True

        return status
