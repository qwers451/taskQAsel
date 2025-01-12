import pytest
from pages.web import ProductPage
from selenium.webdriver import Chrome

# Реализация фикстуры
@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(15)
    yield driver
    driver.quit()

# Функция по проверке осуществления перехода на страницу с вариантом
def test_product_page(browser):
    product_page = ProductPage(browser)
    product_page.load()
    product_page.find_variant()
    # Реализация проверок с помощью PyTest
    assert product_page.blackberry_elements_count() == 6
    assert product_page.dyson_elements_count() == 1
    assert product_page.hp_elements_count() == 1
    assert product_page.lg_elements_count() == 1
    assert product_page.nokia_elements_count() == 1
    assert product_page.samsung_elements_count() == 1
    assert product_page.heading_images_count() == 1
    assert product_page.title_elements_count() == 1