import requests
import allure

from data import Urls


class CourierPage:

    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(payload):
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(Urls.CREATE_COURIER, data=payload, timeout=20)
        return response

    @staticmethod
    @allure.step("Авторизация курьера")
    def log_in_courier(payload):
        # отправляем запрос на авторизацию курьера и сохраняем ответ в переменную response
        response = requests.post(Urls.LOGIN_COURIER, data=payload, timeout=20)
        return response