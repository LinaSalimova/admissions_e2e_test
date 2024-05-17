import allure
import pytest

from selene import browser, have

button_submit_documents = '.link-action'

last_name = '#family_guest'
first_name = '#name_guest'
surname = '#parent_guest'
birthday_input = '#birthday'
button_next = '#reg-nextStep'
choice_country = '#citizenship'
city = '#city'
phone = '#phone'
email = '#email'
password = '#password_set'
password_repeat = '#password_repeat'
agreement = '#agreement'
button_registration = '#regSubmit'


class RegistrationPage:

    @allure.step('Enter registration details № 1')
    def registration_add_value_part_1(self):
        browser.element(button_submit_documents).type('last_name')
        browser.element(first_name).click().type('first_name')
        browser.element(surname).click().type('surname')
        browser.element(birthday_input).click().type('01.01.1991')
        browser.element(button_next).click()
        return self

    @allure.step('Enter registration details № 2 ')
    def registration_add_value_part_2(self):
        browser.element(choice_country).element_by(have.text('Иностранный гражданин')).click()
        browser.element(city).click().type('Paris city')
        browser.element(phone).click().type('+33769211222')
        browser.element(email).click().type('france@gmail.com')
        browser.element(password).click().type('123423sdfzxcE')
        browser.element(password_repeat).click().type('123423sdfzxcE')
        browser.element(agreement).click()
        browser.element(button_registration).click()
        return self

    @allure.step('Registration check')
    def check_for_success(self):
        assert 'https://abiturient.kpfu.ru/entrant/abit_registration.registration_script'
