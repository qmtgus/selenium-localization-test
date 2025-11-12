import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Добавляем опцию командной строки --language
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help='Specify browser language (e.g., ru, en, fr)')


@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение параметра language из командной строки
    user_language = request.config.getoption("language")
    print(f"\nЗапуск Chrome с языком: {user_language}")

    # Настройка опций Chrome для установки нужного языка
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Инициализация браузера
    browser = webdriver.Chrome(options=options)

    yield browser

    # Закрытие браузера
    print("\nЗавершение работы браузера...")
    browser.quit()