import allure
from bs4 import BeautifulSoup
from selene import browser


class MenuListPage:
    # 1. открыть стр
    @allure.step('Open page')
    def open_admission_rules(self):
        browser.element('.menuLevel3__item').click()
        return self
    # 2. проверить наличие файла (реализовать парсер с проверкой наличия файла) добавить выведение эксепшенов
    @allure.step('Check for file existence')
    def check_existence_file(self):
        main_soup = BeautifulSoup(html, 'html.parser')
        required_part_of_soup = BeautifulSoup(str(main_soup.find(class_='link-doc')), 'html.parser')
        for link in required_part_of_soup.find_all('a'):
            print(link.get('href'))
    # 3. открыть выпадающие окна и проверить текст

    # 4. открыть следующий блок
