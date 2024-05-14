import allure

from selene import browser, have, be


class HomePage:


# Открываем url

    @allure.step('Open main page')
    def open(self):
        browser.open('')
# ищим лого
    @allure.step('Logo check')
    def confirm_logo(self):
        logo = browser.element('.logo--mob')
        assert logo(browser, object)
# смотрим работает ли меню
    @allure.step('Check the availability and operability of the navigation menu')
    def operability_navigation_menu(self,value):
        browser.element('.openMenu').should(have.text('меню')).click()
        browser.element('#signin').should(have.text('Личный кабинет'))
        browser.element('.openMenu_active').click()
# смотрим отображаются ли новости
    @allure.step('Check the display of the slider with news or announcements')
    def check_news(self):
        browser.element('.col-6 col-sm-3').click()

# проверяем футтер
    @allure.step('Footer performance')
    def check_footer(self):
        browser.all('.container').second.should(have.text('420008, г. Казань, ул. Кремлевская, д. 35, каб. 114, 115, 211'))
