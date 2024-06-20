from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By


class Reg(BasePage):
    # Input fields
    input_firstname = (By.CSS_SELECTOR, "#input-firstname")
    input_lastname = (By.CSS_SELECTOR, "#input-lastname")
    input_email = (By.CSS_SELECTOR, "#input-email")
    input_telephone = (By.CSS_SELECTOR, "#input-telephone")
    input_password = (By.CSS_SELECTOR, "#input-password")
    input_confirm_password = (By.CSS_SELECTOR, "#input-confirm")

    # Buttons
    button_acceptance = (By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]")
    button_next = (By.XPATH, "//body/div[@id='account-register']/div[1]/div[1]/form[1]/div[1]/div[1]/input[2]")
