import time

import pytest
from selenium.webdriver.common.by import By

from pageobjectmodule.AccountSuccesspage import AccountSuccessPage
from pageobjectmodule.Homepage import HomePage
from pageobjectmodule.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest


#@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister(BaseTest):
    def test_create_account_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Arun1235", "Motoori3456",
                                                                 self.generate_email_time_stamp(), "0987654321",
                                                                 "12345", "12345", "no", "select")

        register_text = "Your Account Has Been Created!"

        assert account_success_page.retrieve_account_creation_message().__eq__(register_text)

    def test_create_account_by_providing_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()

        account_success_page = register_page.register_an_account("Arun1235", "Motoori3456",
                                                                 self.generate_email_time_stamp(), "0987654321",
                                                                 "12345", "12345", "yes", "select")

        register_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(register_text)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()

        register_page.register_an_account("Arun1235", "Motoori3456", "amotooricap3@gmail.com", "0987654321", "12345",
                                          "12345", "yes", "select")

        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__eq__(
            expected_warning_message)

    def test_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()

        register_page.register_an_account("", "", "", "", "", "", "no", "no")

        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!", "First Name must be "
                                                                                                   "between 1 and 32 "
                                                                                                   "characters!",
                                                 "Last Name must be between 1 and 32 characters!", "E-Mail Address "
                                                                                                   "does not appear to"
                                                                                                   " be valid!",
                                                 "Telephone must be between 3 and 32 characters!",
                                                 "Password must be between 4 and 20 characters!")

    # def generate_email_time_stamp(self):
    #     timestamp = time.strftime('%Y%m%d%H%M%S')
    #     return "arun" + timestamp + "@gmail.com"
