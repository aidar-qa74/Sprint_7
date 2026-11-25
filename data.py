class Urls:

    MAIN_PAGE_URL = 'http://qa-scooter.praktikum-services.ru' #Основная ссылка

    LOGIN_COURIER = MAIN_PAGE_URL + '/api/v1/courier/login' # POST-запрос. Логин курьера в системе
    CREATE_COURIER = MAIN_PAGE_URL + '/api/v1/courier' # POST-запрос. Создание курьера в системе

    ORDERS_URL = MAIN_PAGE_URL + '/api/v1/orders' # GET-запрос. Получение списка заказов // POST-запрос. Создание заказа
class OrderPageData:
    # Данные для заказа самоката
    DATA_ORDER_1 = {
        'first_name': 'Тест',
        'last_name': 'Тестов',
        'address': 'Тестовая, 12',
        'station': 'Сокольники',
        'tel_number': '+79998887766',
        'delivery_date': '27.11.2026',
        'rent_days': 'двое суток',
        #'scooter_colour': 'black',
        'comment': 'Тестовый комментарий!'}

class HttpStatusCode:
    HTTP_STATUS_OK = 200           # универсальный статус удачного запроса
    HTTP_STATUS_CREATED = 201      # статус создания новых записей
    HTTP_STATUS_CONFLICT = 409     # статус 409 для конфликтов
    HTTP_STATUS_BAD_REQUEST = 400  # только статус 400 для некорректных запросов
    HTTP_STATUS_NOT_FOUND = 404   # статус 404 для "не найдено"
class ErrorMessages:
    ERROR_MESSAGE_LOGIN_DUPLICATE = "Этот логин уже используется. Попробуйте другой."
    ERROR_MESSAGE_MISSING_FIELDS_CREATE_COURIER = "Недостаточно данных для создания учетной записи"
    ERROR_MESSAGE_MISSING_FIELDS_LOG_IN_COURIER = "Недостаточно данных для входа"
    ERROR_MESSAGE_NOT_FOUND = "Учетная запись не найдена"

TEXT_SUCCESFUL_REQUEST = '{"ok":true}'