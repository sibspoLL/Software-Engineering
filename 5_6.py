import re  # Импорт модуля для работы с регулярными выражениями
import sys  # Импорт модуля для работы с системными функциями

def strip_punctuation_ru(data):
    # Определение шаблона для поиска знаков препинания на русском языке
    punctuation_pattern = r"[!\"#$%&'()*+,-./:;<=>?@\[\\\]^_`{|}~«»]"

    # Замена знаков препинания на пробелы, за исключением точек, которые остаются
    stripped_text = re.sub(punctuation_pattern, lambda match: " " if match.group() != "." else "", data)

    # Удаление лишних пробелов и объединение слов
    return " ".join(stripped_text.split())

# Чтение строки из ввода и удаление лишних пробелов
input_string = sys.stdin.readline().strip()

# Вывод результата работы функции strip_punctuation_ru для введенной строки
print(strip_punctuation_ru(input_string))

def test_strip_punctuation_ru():
    # Тестовые данные и ожидаемые результаты
    test_data = [
        'Привет, как дела?',
        'Сегодня - отличная погода!',
        'Тест: 1, 2, 3... Проверка.',
        'Это предложение без знаков препинания'
    ]
    expected_results = [
        'Привет как дела',
        'Сегодня отличная погода',
        'Тест 1 2 3 Проверка',
        'Это предложение без знаков препинания'
    ]

    # Перебор тестовых данных и проверка на соответствие ожидаемым результатам
    for data, expected in zip(test_data, expected_results):
        if strip_punctuation_ru(data) != expected:  # Если результат отличается от ожидаемого
            print("NO")  # Выводим "NO"
            return
    print("YES")  # Если все тесты пройдены успешно, выводим "YES"

# Запуск тестовой программы
test_strip_punctuation_ru()
