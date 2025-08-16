from selenium.webdriver.common.by import By

class FeedPageLocators:
    HEADER_ASSEMBLE_BURGER = (By.XPATH,
                         ".//*[@class='text text_type_main-large mt-10 mb-5'][text()='Лента заказов']")
    ORDER_BURGER = (By.XPATH,
                              ".//*[@class='text text_type_digits-default']")
    DETAILS_BURGER = (By.XPATH,
                    ".//*[@class='text text_type_main-medium mb-8'][text()='Cостав']")
    COUNTER_ORDER_ALL_TIME = (By.XPATH,
                      ".//*[@class='undefined mb-15']//*[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    COUNTER_ORDER_TODAY = (By.XPATH,
                              ".//*[@class='text text_type_main-medium'][text()='Выполнено за сегодня:']/following-sibling::p[1]")
    NUMBER_ORDER = (By.XPATH,
                    ".//*[@class='text text_type_digits-default'][text()='#0280801']")
    ORDER_IN_PROGRESS = (By.XPATH,
                    ".//*[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']//*[@class='text text_type_digits-default mb-2']")