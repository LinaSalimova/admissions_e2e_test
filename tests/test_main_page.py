import allure
import pytest

from allure_commons.types import Severity

from data.filter import tags, page_munu
from pages import registration_page


@allure.tag("ui", "web")
@allure.label('owner', 'Alina Salimova')
@allure.feature('UI')
@allure.story('Checking home page accessibility')
@allure.severity(Severity.NORMAL)
class CheckingHomePage:


def test_сhecking_home_page(self, setup_browser):
    with allure.step('Open home page'):
        home_page.open()
    with allure.step('Check logo,menu,footer'):
        home_page.confirm_logo()
        home_page.operability_navigation_menu()
        home_page.check_news()
        home_page.check_footer()


@allure.tag("ui", "web")
@allure.label('owner', 'Alina Salimova')
@allure.feature('UI')
@allure.story('Checking home page accessibility')
@allure.severity(Severity.NORMAL)
class DegreeScenarioPage:
    @pytest.mark.parametrize('container', [tags])
    @pytest.mark.parametrize('page', [page_munu])


def test_check_page(container, page):
    menu_list_page.open_admission_rules()
    menu_list_page.check_existence_file()


@allure.tag("ui", "web")
@allure.label('owner', 'Alina Salimova')
@allure.feature('UI')
@allure.story('Registration')
@allure.severity(Severity.NORMAL)
class RegistrationPage:
    def test_check_page(self, setup_browser):
    registration_page.registration_add_value()
