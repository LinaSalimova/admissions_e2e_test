import allure

from allure_commons.types import Severity

from pages import home_page


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
class BachelorPage:

    def test_сhecking_home_page(self, setup_browser):
