from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def test_find_cart_button(browser):
  link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

  # Переменная для проверки условия в assert
  cart_button = None

  try:
    browser.get(link)
    # time.sleep(30)

    # Ищем кнопку добавления в корзину
    cart_button = browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')

  # Ловим ошибку, если кнопка не найдена
  except NoSuchElementException:
    assert cart_button is not None, 'Кнопка добавления в корзину не найдена'


