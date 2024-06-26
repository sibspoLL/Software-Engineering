import re

def check_string(string):
    # Удаляем все нечисловые символы в начале слова, кроме знака +, чтобы остались только цифры и знак + для номера телефона
    phone = re.sub(r'\b\D', '', string)
    # Убираем пробелы и скобки, чтобы остались только цифры и знак + для номера телефона
    clear_phone = re.sub(r'[\ \(]?', '', phone)
    # Проверяем, соответствует ли строка формату российского номера телефона или email
    # Формат номера телефона: начинается с +7 или 8, далее 10 цифр
    # Формат email: стандартный формат с символом @ и доменной частью
    if re.findall(r'^[\+7|8]*?\d{10}$', clear_phone) or re.match(r'^\w+[\.]?(\w+)*\@(\w+\.)*\w{2,}$', string):
        return bool(string)  # Возвращаем True, если строка соответствует одному из форматов
    else:
        return False  # Возвращаем False, если строка не соответствует ни одному из форматов
# Читаем строку из ввода пользователя и проверяем ее с помощью функции check_string, затем печатаем результат
print(check_string(input()))





def is_correct_mobile_phone_number_ru(number):
    # Удаляем пробелы, дефисы и скобки из строки номера телефона для упрощения проверки
    cleaned_number = re.sub(r'[ \-\(\)]', '', number)

    # Проверяем, соответствует ли очищенный номер формату: начинается с +7 или 8 и содержит 10 цифр после этого
    return bool(re.match(r'^(\+7|8)\d{10}$', cleaned_number))

def test_is_correct_mobile_phone_number_ru():
    # Словарь тестовых случаев, где ключ - номер телефона, а значение - ожидаемый результат
    test_cases = {
        "+7 900 123 45 67": True,  # Номер с пробелами, корректный
        "+7(900)1234567": True,    # Номер со скобками, корректный
        "8 900 123-45-67": True,   # Номер с пробелами и дефисами, корректный
        "8(900)123 4567": True,    # Номер со скобками и пробелами, корректный
        "89001234567": True,       # Чистый номер, корректный
        "7 900 1234567": False,    # Номер, начинающийся с 7, некорректный
        "+79001234567": True,      # Чистый номер с +7, корректный
        "+7 900 123 45": False,    # Номер с недостаточным количеством цифр, некорректный
        "+7 900 123 45 678": False,# Номер с лишними цифрами, некорректный
        "8 900 123 45": False      # Номер с недостаточным количеством цифр, некорректный
    }

    # Флаг, указывающий на то, что все тесты пройдены
    all_tests_passed = True

    # Перебираем все тестовые случаи
    for number, expected_result in test_cases.items():
        # Проверяем, совпадает ли результат вызова is_correct_mobile_phone_number_ru с ожидаемым результатом
        if is_correct_mobile_phone_number_ru(number) != expected_result:
            all_tests_passed = False
            break

    # Если все тесты пройдены, печатаем YES, иначе NO
    if all_tests_passed:
        print("YES")
    else:
        print("NO")

# Запускаем тестирующую программу
test_is_correct_mobile_phone_number_ru()
