import allure

from allure_commons.types import Severity
from pages.main_page import MainPage

main_page = MainPage()


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Alina Salimova')
@allure.feature('Main page')
@allure.story('Checking home page accessibility')
@allure.link('https://admissions.kpfu.ru/')
def test_сhecking_home_page():
    main_page.open()
    main_page.confirm_logo()
    main_page.operability_navigation_menu()
    main_page.check_news()
    main_page.check_footer()
    pass


@allure.tag('Web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Alina Salimova')
@allure.feature('Bachelor page')
@allure.story('Checking the training program filtering system')
@allure.link('https://admissions.kpfu.ru/')
def test_go_to_page():
    main_page.open()
    main_page.go_to_bachelor()
    main_page.confirm_contacts_page()

