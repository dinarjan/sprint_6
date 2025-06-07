from pages.base_page import BasePage
import allure
from locators.order_locators import OrderLocators
from locators.questions_locators import QuestionsLocators


class MainPage(BasePage):
    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_upper_order_button(self):
        self.click(OrderLocators.UPPER_ORDER_BUTTON)

    @allure.step('Листаем страницу и нажимаем на нижнюю кнопку "Заказать"')
    def click_lower_order_button(self):
        self.scroll_to_element(OrderLocators.LOWER_ORDER_BUTTON)
        self.click(OrderLocators.LOWER_ORDER_BUTTON)

    @allure.step('Получаем текст вопроса и ответа')
    def get_qa_text(self, loc_question, loc_answer):
        q_text = self.get_text(loc_question)
        self.click(loc_question)
        a_text = self.get_text(loc_answer)
        return q_text, a_text

    @allure.step('Листаем страницу до вопросов ')
    def scroll_to_list_qa(self):
        self.scroll_to_element(QuestionsLocators.question_8)
