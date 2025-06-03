from selenium.webdriver.common.by import By


class OrderLocators:
    UPPER_ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g')
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION = (By.XPATH, "//div[@class='select-search__value']/child::input[@placeholder='* Станция метро']")
    PHONE_NUMBER = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT = (By.XPATH, "//div[@class='Order_NextButton__1_rCA']/child::button[text()='Далее']")
    DELIVER_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    TIME_LIMIT = (By.XPATH, "//div[text()='* Срок аренды']")
    TIME_LIMIT_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-menu']/div[text()='сутки']")
    COLOR = (By.XPATH, "//label[text()='чёрный жемчуг']")
    SUBMIT_ORDER = (By.XPATH, " //div[@class='Order_Buttons__1xGrp']/child::button[text()='Заказать']")
    YES = (By.XPATH, " //div[@class='Order_Buttons__1xGrp']/child::button[text()='Да']")
    SUCCESS_WINDOW = (By.XPATH, "//div[text()='Заказ оформлен']")
    VIEW_STATUS = (By.XPATH, "//div[@class='Order_NextButton__1_rCA']/child::button[text()='Посмотреть статус']")
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
    YANDEX_POP_UP = (By.XPATH, "//div[text()='Установить Яндекс Браузер?']")
    LOWER_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
