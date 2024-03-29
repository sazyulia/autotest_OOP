from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .pages.product_page import ProductPage
#from .pages.login_page import LoginPage
import time

def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_present_in_cart()
    page.should_check_overall_cost()