import re

def is_correct_mobile_phone_number_ru(number):
    # Удаляем пробелы, дефисы и скобки из строки номера телефона для упрощения проверки
    cleaned_number = re.sub(r'[ \-\(\)]', '', number)

    # Проверяем, соответствует ли очищенный номер формату: начинается с +7 или 8 и содержит 10 цифр после этого
    return bool(re.match(r'^(\+7|8)\d{10}$', cleaned_number))

# Считываем строку из стандартного ввода
number = input().strip()

# Проверяем, является ли строка корректным номером мобильного телефона для России
if is_correct_mobile_phone_number_ru(number):
    print("YES")
else:
    print("NO")
