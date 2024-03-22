import pytest
from selenium.webdriver.common.by import By

from pageobjectmodule import Searchpage
from pageobjectmodule.Homepage import HomePage
from pageobjectmodule.Searchpage import SearchPage
from tests.BaseTest import BaseTest


# @pytest.mark.usefixtures("setup_and_teardown")
class TestSearch(BaseTest):
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("HP")
        # home_page.enter_product_into_search_box_filed("HP")
        # search_page = home_page.click_on_search_button()
        assert search_page.display_status_of_valid_product()

    def test_Search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("HONDA")
        # home_page.enter_product_into_search_box_filed("HONDA")
        # search_page = home_page.click_on_search_button()
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(expected_text)

    def test_Search_without_providing_any_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("")
        # home_page.enter_product_into_search_box_filed("")
        # search_page = home_page.click_on_search_button()
        expected_text = "There is no product that matches the search criteria.ABC"
        assert search_page.retrieve_no_product_message().__eq__(expected_text)
