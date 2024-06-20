from conftest import *
from page_objects.MainPage import MainPage
from page_objects.ProductPage import ProductPage
from page_objects.Reg import Reg


@allure.feature("Main picture")
@allure.title("Clicking left in picture")
def test_1(driver):
    MainPage(driver).click(MainPage.macbook_link)
    ProductPage(driver).click(ProductPage.main_images_product)
    ProductPage(driver).left().left().left()


@allure.feature("Shopping Products")
@allure.title("Add macbook to cart")
def test_2(driver):
    MainPage(driver).click(MainPage.macbook_link)
    MainPage(driver).click(ProductPage.add_to_cart_button)


@allure.feature("Main page navbar")
@allure.title("Check computer in store")
def test_3(driver):
    MainPage(driver).click(MainPage.computer_dropdown)
    MainPage(driver).click(MainPage.computer_dropdown_button)


@allure.feature("Registration")
@allure.title("Check registration")
def test_4(driver):
    MainPage(driver).click(MainPage.button_to_choose_registration)
    MainPage(driver).click(MainPage.button_to_registration)
    Reg(driver).input(Reg.input_firstname, "first name")
    Reg(driver).input(Reg.input_lastname, "last name")
    Reg(driver).input(Reg.input_email, "email33@mail.ru")
    Reg(driver).input(Reg.input_telephone, "89999999999")
    Reg(driver).input(Reg.input_password, "QwErTy@")
    Reg(driver).input(Reg.input_confirm_password, "QwErTy@")
    Reg(driver).click(Reg.button_acceptance)
    Reg(driver).click(Reg.button_next)


@allure.feature("Search")
@allure.title("Input text in search")
def test_5(driver):
    MainPage(driver).input(MainPage.search_field, "mouse")


@allure.feature("Add product to cart")
@allure.title("Add macbook to cart")
def test_6(driver):
    MainPage(driver).click(MainPage.macbook_link)
    MainPage(driver).click(ProductPage.add_to_favorites_button)


def test_7(driver):
    MainPage(driver).click(MainPage.macbook_link)
    MainPage(driver).click(ProductPage.add_to_cart_button)


@allure.title("Add samsung to cart")
def test_8(driver):
    MainPage(driver).click(MainPage.tablets_dropdown)
    MainPage(driver).click(MainPage.samsung_galaxy_tab_link)
    MainPage(driver).click(ProductPage.add_to_cart_button)


@allure.title("Add iPhone to cart")
def test_9(driver):
    MainPage(driver).click(MainPage.phones_dropdown)
    MainPage(driver).click(MainPage.iphone_link)
    MainPage(driver).click(ProductPage.add_to_cart_button)


@allure.feature("Add review to product")
@allure.title("Add review to macbook")
def test_10(driver):
    MainPage(driver).click(MainPage.macbook_link)
    ProductPage(driver).click(ProductPage.review_tab)
    ProductPage(driver).input(ProductPage.review_name_input, "NAME")
    ProductPage(driver).input(ProductPage.review_text_input, "TESTTESTTESTTESTTESTTESTTESTTESTTESTTEST")
    ProductPage(driver).click(ProductPage.review_rating_input)
    ProductPage(driver).click(ProductPage.submit_review_button)
