from selenium.webdriver.common.by import By

class ProductPage:
    URL = 'https://qa-test-selectors.netlify.app/'
    VARIANT = 31
    HEADING = "BlackBerry"
    TITLE_TEXT = "Samsung"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def find_variant(self):
        button = self.browser.find_element(By.CSS_SELECTOR,
        f'.variant__btn:nth-child({self.VARIANT})')
        # Нажатие на кнопку с вариантом
        button.click()

    def blackberry_elements_count(self):
        # Поиск элементов с data-type="blackBerry"
        tree_elements = self.browser.find_elements(By.XPATH,
        '//*[@data-type="blackBerry"]')
        return len(tree_elements)

    def dyson_elements_count(self):
        # Поиск элементов с id="dyson"
        dyson_elements = self.browser.find_elements(By.ID, 'dyson')
        return len(dyson_elements)

    def hp_elements_count(self):
        # Поиск элементов с class="hp"
        hp_elements = self.browser.find_elements(By.CLASS_NAME, 'hp')
        return len(hp_elements)

    def lg_elements_count(self):
        # Поиск элементов с name="lg"
        lg_elements = self.browser.find_elements(By.NAME, 'lg')
        return len(lg_elements)

    def nokia_elements_count(self):
        # Поиск элементов с data-type="nokia"
        nokia_elements = self.browser.find_elements(By.XPATH,
        '//*[@data-type="nokia"]')
        return len(nokia_elements)

    def samsung_elements_count(self):
        # Поиск элементов с class="samsung"
        samsung_elements = self.browser.find_elements(By.CLASS_NAME, 'samsung')
        return len(samsung_elements)

    def heading_images_count(self):
        # Поиск изображений с heading="BlackBerry"
        heading_images = self.browser.find_elements(By.XPATH,
        f'//img[@heading="{self.HEADING}"]')
        return len(heading_images)

    def title_elements_count(self):
        # Поиск элементов с name="Samsung"
        title_elements = self.browser.find_elements(By.XPATH,
        f'//h1[text()="{self.TITLE_TEXT}"]')
        return len(title_elements)


