from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = browser.find_element("xpath", "//input[@placeholder='First Name']")
    LAST_NAME = browser.find_element("xpath", "//input[@placeholder='Last Name']")
    EMAIL = browser.find_element("xpath", "//input[@placeholder='name@example.com']")
    GENDER = browser.find_element(By.CSS_SELECTOR, "label[for='gender-radio-3']")
    MOBILE = browser.find_element("xpath", "//input[@placeholder='Mobile Number']")
    SUBJECT = browser.find_element("xpath", "//div[@class='subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3']")
    HOBBIES = browser.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
    UPLOAD_PIC = browser.find_element(By.ID, "uploadPicture")
    UPLOAD_PIC.send_keys("C:\\Users\\adika\\Downloads\\english_class.txt")
    CURRENT_ADRESS = browser.find_element("xpath", "//input[@placeholder='Current Address']")
    SUBMIT =
