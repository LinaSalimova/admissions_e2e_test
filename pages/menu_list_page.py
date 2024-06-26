from cgitb import html

import allure
import requests
from bs4 import BeautifulSoup
from selene import browser

menu_type_education = '.fastMenu__link'


class MenuListPage:

    # 1. открыть стр
    @allure.step('Open type education')
    def open_admission_rules(self):
        browser.element(menu_type_education).click()
        return self

    # 2. проверить наличие файла (реализовать парсер с проверкой наличия файла) добавить выведение эксепшенов
    @allure.step('Check for file existence')
    def check_existence_file(self):
        requests.get(browser.config.base_url)
        main_soup = BeautifulSoup(html, 'html.parser')
        required_part_of_soup = BeautifulSoup(str(main_soup.find(class_='link-doc')), 'html.parser')
        for link in required_part_of_soup.find_all('.pdf'):
            print(link.get('href'))
    # 3. открыть выпадающие окна и проверить текст

    collapseBlock__title

