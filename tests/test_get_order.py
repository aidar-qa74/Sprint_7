import allure

from pages.order_api import OrderPage
from data import HttpStatusCode

class TestGetOrder:

    @allure.title("Проверь, что в тело ответа возвращается список заказов")

    def test_get_list_orders(self):
        response = OrderPage.get_all_orders()
        assert response.status_code == HttpStatusCode.HTTP_STATUS_OK and len(response.json()['orders'])>0