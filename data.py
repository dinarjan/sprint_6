from locators.questions_locators import QuestionsLocators

MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
DZEN_PAGE = 'https://dzen.ru/?yredirect=true'

text_faq = [
    {
        "text_question": "Сколько это стоит? И как оплатить?",
        "text_answer": "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "loc_question": QuestionsLocators.question_1,
        "loc_answer": QuestionsLocators.answer_1
    },
    {
        "text_question": "Хочу сразу несколько самокатов! Так можно?",
        "text_answer": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "loc_question": QuestionsLocators.question_2,
        "loc_answer": QuestionsLocators.answer_2
    },
    {
        "text_question": "Как рассчитывается время аренды?",
        "text_answer": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "loc_question": QuestionsLocators.question_3,
        "loc_answer": QuestionsLocators.answer_3
    },
    {
        "text_question": "Можно ли заказать самокат прямо на сегодня?",
        "text_answer": "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "loc_question": QuestionsLocators.question_4,
        "loc_answer": QuestionsLocators.answer_4
    },
    {
        "text_question": "Можно ли продлить заказ или вернуть самокат раньше?",
        "text_answer": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "loc_question": QuestionsLocators.question_5,
        "loc_answer": QuestionsLocators.answer_5
    },
    {
        "text_question": "Вы привозите зарядку вместе с самокатом?",
        "text_answer": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "loc_question": QuestionsLocators.question_6,
        "loc_answer": QuestionsLocators.answer_6
    },
    {
        "text_question": "Можно ли отменить заказ?",
        "text_answer": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "loc_question": QuestionsLocators.question_7,
        "loc_answer": QuestionsLocators.answer_7
    },
    {
        "text_question": "Я жизу за МКАДом, привезёте?",
        "text_answer": "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
        "loc_question": QuestionsLocators.question_8,
        "loc_answer": QuestionsLocators.answer_8
    }
]

order_data = [
    {
        "id": 0,
        "name": "Динар",
        "surname": "Буранбаев",
        "address": "ул. Ахметова 316",
        "station": "Черкизовская",
        "phone_number": "+79199191919",
        "rental_period": "15.06.2025"
    },
    {
        "id": 1,
        "name": "Иван",
        "surname": "Иванов",
        "address": "ул. Октября 99 ",
        "station": "Сокольники",
        "phone_number": "+79279278456",
        "rental_period": "20.06.2025"
    }
]
