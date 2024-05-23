from locators.form_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FIRST_NAME).send_keys("Name")
        self.element_is_visible(self.locators.LAST_NAME).send_keys("Secname")
        self.element_is_visible(self.locators.EMAIL).send_keys("myemail@dog.com")
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys("0000000000")
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_visible(self.locators.UPLOAD_PIC).send_keys("C:\\Users\\adika\\Downloads\\english_class.txt")
        self.element_is_visible(self.locators.CURRENT_ADRESS).send_keys("Pushkina Str, House of Kolotushkina")
        self.element_is_visible(self.locators.SUBJECT).send_keys("English")
        self.element_is_visible(self.locators.SUBJECT).click()
        self.element_is_visible(self.locators.SUBMIT).click()

