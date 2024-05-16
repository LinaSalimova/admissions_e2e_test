import allure

from selene import browser, have

button_open_menu = '.openMenu'
check_button_sign_in = '#signin'
button_menu_close = '.hamburger_burger1'
logo = '.logo--mob'
view_all_news = '.col-6 col-sm-3'


class HomePage:
    # 1.Открываем url
    @allure.step('Open main page')
    def open(self):
        browser.open('')
        return self

    # 2. Ищим лого
    @allure.step('Logo check')
    def confirm_logo(self):
        browser.element(logo)
        return self
    # 3.Смотрим работает ли меню
    @allure.step('Check the availability and operability of the navigation menu')
    def operability_navigation_menu(self):
        browser.element(button_open_menu).should(have.text('меню')).click()
        browser.element(check_button_sign_in).should(have.text('Личный кабинет'))
        browser.element(button_menu_close).click()
        return self
    # 4.Смотрим отображаются ли новости
    @allure.step('Check the display of the slider with news or announcements')
    def check_news(self):
        browser.element(view_all_news).click()
        return self
    # 5.Проверяем футтер
    @allure.step('Footer performance')
    def check_footer(self):
        browser.all('.container').second.should(
            have.text('420008, г. Казань, ул. Кремлевская, д. 35, каб. 114, 115, 211'))
        return self