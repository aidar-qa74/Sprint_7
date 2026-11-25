import allure
import pytest

from pages.courier_api import CourierPage
from data import TEXT_SUCCESFUL_REQUEST, HttpStatusCode, ErrorMessages

class TestCreateCourier:
    @allure.title('Курьера можно создать, успешный запрос возвращает правильный код')
    def test_create_courier_success(self,valid_courier_payload):
        response  = CourierPage.create_courier(valid_courier_payload)
        assert response.status_code == HttpStatusCode.HTTP_STATUS_CREATED and response.text == TEXT_SUCCESFUL_REQUEST

    @allure.title('Нельзя создать 2 одинаковых курьеров')
    @allure.description('Ecли создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_create_courier_with_login_already_exists_error(self, valid_courier_payload):
        CourierPage.create_courier(valid_courier_payload)
        response_courier_duplicate = CourierPage.create_courier(valid_courier_payload)
        assert response_courier_duplicate.status_code == HttpStatusCode.HTTP_STATUS_CONFLICT and response_courier_duplicate.json()["message"] == ErrorMessages.ERROR_MESSAGE_LOGIN_DUPLICATE

    @pytest.mark.parametrize('empty_fields', ['login', 'password', 'firstName'])
    @allure.title('Чтобы создать курьера, нужно передать в ручку все обязательные поля, проверка пустого поля: {empty_fields}')
    @allure.description('Если одного из полей нет, запрос возвращает ошибку')
    def test_create_courier_with_empty_fields_error(self,valid_courier_payload, empty_fields):
        #Удаление одного из полей
        valid_courier_payload.pop(empty_fields)
        response = CourierPage.create_courier(valid_courier_payload)
        assert response.status_code == HttpStatusCode.HTTP_STATUS_BAD_REQUEST and response.json()["message"] == ErrorMessages.ERROR_MESSAGE_MISSING_FIELDS_CREATE_COURIER