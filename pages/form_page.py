from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
from selenium.webdriver.common.keys import Keys
from generator.generator import generated_person, generated_file
import os

class FormPage(BasePage):

    def fill_fields_and_submit(self):
        person = genegated_person()
        path = generated_file()
        subject = self.element_is_visible(self.locators.SUBJECT)
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_visible(self.locators.UPLOAD_PIC).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        result_text = []
        for i in result_list:
            result_text.append(i.text)
        return result_text


