from selenium.webdriver.common.by import By


class FeedPageLocators:
    HEADER_ASSEMBLE_BURGER = (By.XPATH,
                         ".//*[@class='text text_type_main-large mt-10 mb-5'][text()='Лента заказов']")