import allure
import pytest

from pages.order_api import OrderPage
from data import OrderPageData, HttpStatusCode

class TestCreateOrderColors:

    @pytest.mark.parametrize('colors', [['black'],['grey'],['black', 'grey'], None])
    @allure.title("можно создать создать заказ с выбором цвета, тело ответа содержит track")
    @allure.description("можно указать один из цветов — BLACK или GREY; можно указать оба цвета; можно совсем не указывать цвет")

    def test_create_order_with_colors(self, colors):
        payload = OrderPageData.DATA_ORDER_1.copy()
        payload['color'] = colors
        response = OrderPage.create_order(OrderPageData.DATA_ORDER_1)
        assert response.status_code == HttpStatusCode.HTTP_STATUS_CREATED and response.json()['track']

    @allure.title("возможность создать заказ без выбора цвета")
    def test_create_order_without_colors(self):
        response = OrderPage.create_order(OrderPageData.DATA_ORDER_1)
        assert response.status_code == HttpStatusCode.HTTP_STATUS_CREATED and response.json()['track']