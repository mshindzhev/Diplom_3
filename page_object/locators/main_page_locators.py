from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH,
                               ".//*[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Личный Кабинет']")
    BUTTON_CONSTRUCTOR = (By.XPATH,
                          ".//*[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Конструктор']")
    BUTTON_ORDER_FEED = (By.XPATH,
                         ".//*[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Лента Заказов']")
    HEADER_ASSEMBLE_BURGER = (By.XPATH,
                              ".//*[@class='text text_type_main-large mb-5 mt-10'][text()='Соберите бургер']")
    HEADER_DETAILS_INGREDIENT = (By.XPATH,
                                 ".//*[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10'][text()='Детали ингредиента']")
    BUTTON_CLOSE_DETAILS_MODAL = (By.XPATH,
                                  ".//*[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//*[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    COUNTER_INGREDIENT = (By.XPATH,
                          ".//*[@href='/ingredient/61c0c5a71d1f82001bdaaa72']//*[@class='counter_counter__num__3nue1']")
    INGREDIENT = (By.XPATH,
                  ".//*[@href='/ingredient/61c0c5a71d1f82001bdaaa72']//*[@class='BurgerIngredient_ingredient__image__3e-07 ml-4 mr-4']")
    LIST_INGREDIENTS_BURGER_CONSTRUCTOR = (By.XPATH,
                                           ".//*[@class='BurgerConstructor_basket__listContainer__3P_AM']")
    BUTTON_CREATE_ORDER = (By.XPATH,
                           ".//*[text()='Оформить заказ']")
    IDENTIFIER_ORDER = (By.XPATH,
                           ".//*[text()='идентификатор заказа']")


