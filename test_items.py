import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Локатор кнопки "Добавить в корзину" (уникальный для этой страницы)
BASKET_BUTTON_SELECTOR = (By.CSS_SELECTOR, ".btn-add-to-basket")
PRODUCT_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    """
    Проверяет, что на странице продукта присутствует кнопка "Добавить в корзину".
    Браузер запускается с языком, указанным в командной строке (--language=...).
    """
    # 1. Открываем страницу товара
    browser.get(PRODUCT_PAGE_URL)

    # 2. time.sleep(30) для визуальной проверки языка интерфейса
    # (Удалить после прохождения задания)
    print("\nВизуальная проверка: 30 секунд. Проверьте, что кнопка на нужном языке.")
    time.sleep(30)

    # 3. Проверка наличия кнопки
    try:
        basket_button = browser.find_element(*BASKET_BUTTON_SELECTOR)
        assert basket_button.is_displayed(), "Кнопка 'Добавить в корзину' найдена, но не отображается"

    except NoSuchElementException:
        # Если элемент не найден, тест падает
        assert False, "Кнопка 'Добавить в корзину' не найдена на странице."

    print("Кнопка 'Добавить в корзину' успешно найдена.")