import allure

from selene import browser

button_submit_documents = '.link-action'

last_name ='#family_guest'
first_name ='#name_guest'
surname ='#parent_guest'
birthday_input='#birthday'
button_next ='#reg-nextStep'
choice_city='#citizenship'
class RegistrationPage:
    @allure.step('Enter registration details № 1')
    def registration_add_value_part_1(self):
        browser.element(button_submit_documents).type('last_name').press_tab()
        browser.element(first_name).click().type('first_name')
        browser.element(surname).click().type('surname')
        browser.element(birthday_input).click().type('01.01.1991')
        browser.element(button_next).click()
        return self

    @allure.step('Enter registration details № 2 ')
    def registration_add_value_part_2(self):
        browser.element(choice_city).click()



    @allure.step('Registration check')
    def check_for_success(self):