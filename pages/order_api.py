import requests
import allure

from data import Urls

class OrderPage:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        response = requests.post(Urls.ORDERS_URL, data=payload, timeout=30)
        return response

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_all_orders():
        response = requests.get(Urls.ORDERS_URL, timeout=60)
        return response