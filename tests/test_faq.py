from pages.main_page import MainPage
from data import text_faq
import allure
import pytest


class TestFAQ:

    @allure.title("Проверка текста вопроса и ответа")
    @pytest.mark.parametrize("data_qa", text_faq)
    def test_faq(self, driver, data_qa):
        main_page = MainPage(driver)
        main_page.open_link()
        main_page.scroll_to_list_qa()
        q_text_expected = data_qa["text_question"]
        a_text_expected = data_qa["text_answer"]
        question_loc = data_qa["loc_question"]
        answer_loc = data_qa["loc_answer"]
        q_text_actual, a_text_actual = main_page.get_qa_text(question_loc, answer_loc)
        assert q_text_expected == q_text_actual, 'Отличается текст вопроса'
        assert a_text_expected == a_text_actual, 'Отличается текст ответа'
