import allure
import pytest

from pages.courier_api import CourierPage
from data import HttpStatusCode, ErrorMessages

class TestLoginCourier:

    @allure.title("Курьер может авторизоваться, успешный запрос возвращает id")
    def test_login_courier_success(self, valid_log_in_payload):
        response = CourierPage.log_in_courier(valid_log_in_payload)
        assert response.status_code == HttpStatusCode.HTTP_STATUS_OK and response.json()['id']

    @pytest.mark.parametrize('empty_fields',['login', 'password'])
    @allure.title("для авторизации нужно передать все обязательные поля, проверка пустого поля {empty_fields}")
    @allure.description("если какого-то поля нет, возвращается ошибка")
    def test_empty_fields_login_courier_error(self, valid_log_in_payload, empty_fields):
        #Удаление одного из полей
        valid_log_in_payload.pop(empty_fields)
        response = CourierPage.log_in_courier(valid_log_in_payload)
        assert response.status_code == HttpStatusCode.HTTP_STATUS_BAD_REQUEST and response.json()['message'] == ErrorMessages.ERROR_MESSAGE_MISSING_FIELDS_LOG_IN_COURIER

    @pytest.mark.parametrize('invalid_data', ['login','password'])
    @allure.title("система вернёт ошибку, если неправильно указать: {invalid_data}")
    @allure.description("если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_invalid_data_login_courier_error_not_found(self, valid_log_in_payload, invalid_data):
        valid_log_in_payload[invalid_data] = 'неверные данные'
        response = CourierPage.log_in_courier(valid_log_in_payload)
        assert response.status_code == HttpStatusCode.HTTP_STATUS_NOT_FOUND and response.json()['message'] == ErrorMessages.ERROR_MESSAGE_NOT_FOUND
