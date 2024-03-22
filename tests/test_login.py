import time

import pytest

from pageobjectmodule.AccountPage import AccountPage
from pageobjectmodule.Homepage import HomePage
from pageobjectmodule.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


# @pytest.mark.usefixtures("setup_and_teardown")
class TestLogin(BaseTest):
    @pytest.mark.parametrize("email_address,password",
                             ExcelUtils.get_data_from_Excel("ExcelFiles/tutorialninja.xlsx", "loginTest"))
    def test_login_with_valid_credentials(self, email_address, password):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        account_page = login_page.login_to_application(email_address,password)
        time.sleep(3)
        assert account_page.display_status_of_edit_your_account_information()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application(self.generate_email_time_stamp(), "Innovation@1990")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("purushotamtewari08@gmail.com", "Innovation@1991")
        time.sleep(2)
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.navigate_to_login_page()
        login_page.login_to_application("", "")
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    # def generate_email_time_stamp(self):
    #     timestamp = time.strftime('%Y%m%d%H%M%S')
    #     return "arun" + timestamp + "@gmail.com"
