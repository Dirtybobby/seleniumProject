from selenium.webdriver.common.by import By
from random import randint


class FormPageLocators:
    FIRST_NAME = ("xpath", "//input[@placeholder='First Name']")
    LAST_NAME = ("xpath", "//input[@placeholder='Last Name']")
    EMAIL = ("xpath", "//input[@placeholder='name@example.com']")
    GENDER = (By.CSS_SELECTOR, f"label[for='gender-radio-{randint(1, 3)}']")
    MOBILE = ("xpath", "//input[@placeholder='Mobile Number']")
    SUBJECT = ("xpath", "//div[@class='subjects-auto-complete__value-container"
                        "subjects-auto-complete__value-container--is-multi css-1hwfws3']")
    HOBBIES = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{randint(1, 3)}']")
    UPLOAD_PIC = (By.ID, "uploadPicture")
    CURRENT_ADDRESS = ("xpath", "//input[@placeholder='Current Address']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")
    RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")