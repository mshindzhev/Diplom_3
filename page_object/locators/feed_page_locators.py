from selenium.webdriver.common.by import By
NUM_ORDER = None
COUNT_ORDERS = None

class FeedPageLocators:
    HEADER_ASSEMBLE_BURGER = (By.XPATH,
                         ".//*[@class='text text_type_main-large mt-10 mb-5'][text()='Лента заказов']")
    ORDER_BURGER = (By.XPATH,
                              f".//*[@class='text text_type_digits-default'][text()={NUM_ORDER}]")
    DETAILS_BURGER = (By.XPATH,
                    ".//*[@class='text text_type_main-medium mb-8']")
    COUNTER_ORDER_ALL_TIME = (By.XPATH,
                      ".//*[@class='undefined mb-15']//*[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    COUNTER_ORDER_TODAY = (By.XPATH,
                              f".//*[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][text()={COUNT_ORDERS}]")