from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
	def should_be_empty_cart(self):
		assert self.is_not_element_present(*CartPageLocators.CART_ITEMS), \
				'Cart is not empty but should be'

	def should_be_empty_cart_message(self):
		empty_cart_message = self.browser.find_element(
				*CartPageLocators.EMPTY_CART_MESSAGE
				).text
		assert 'basket is empty' in empty_cart_message, \
				'Empty cart message is not presented on page, but should be'