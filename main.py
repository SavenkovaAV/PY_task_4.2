# Выбрать (в виде списка) из текста все числа. Числа могут быть
# как целыми, так и вещественными (с разделителем точка или запятая).
import re


def find_numbers_in_file(filename):
    with open(filename, "r") as inputFile:
        text = inputFile.readlines()
        # Используем регулярное выражение для поиска чисел
        pattern = r'[-+]?\d+[\.,]?\d*'
        numbers = []
        for line in text:
            # Находим все числа в тексте
            numbers_in_line = re.findall(pattern, line)
            # Преобразуем строки в числа (если это возможно)
            numbers.extend([float(number.replace(',', '.')) for number in numbers_in_line])
        # Возвращаем список чисел
        return numbers


def test_cases():
    with open("outputTests.txt", "w") as tests:
        # Тест 1: в тексте только целые числа
        if find_numbers_in_file("tests/input01.txt") == [20, 70, 50, 270]:
            tests.write("Test 1: passed.\n")
        else:
            tests.write("Test 1: failed.\n")
            for number in find_numbers_in_file("tests/input01.txt"):
                tests.write(str(number) + "; ")

        # Тест 2: только вещественные числа (с разделителем точка)
        if find_numbers_in_file("tests/input02.txt") == [156.6, 13.01, 12.037, 56.9, 3.2, 182.08]:
            tests.write("Test 2: passed.\n")
        else:
            tests.write("Test 2: failed.\n")
            for number in find_numbers_in_file("tests/input02.txt.txt"):
                tests.write(str(number) + "; ")

        # Тест 3: в файле есть вещественные числа (с разделителем запятая)
        if find_numbers_in_file("tests/input03.txt") == [42.2, 6, 2.5, 140.5]:
            tests.write("Test 3: passed.\n")
        else:
            tests.write("Test 3: failed.\n")
            for number in find_numbers_in_file("tests/input03.txt"):
                tests.write(str(number) + "; ")

        # Тест 4: присутствуют вещественные числа с разными разделителями
        if find_numbers_in_file("tests/input04.txt") == [30.27, 17.73]:
            tests.write("Test 4: passed.\n")
        else:
            tests.write("Test 4: failed.\n")
            for number in find_numbers_in_file("tests/input04.txt"):
                tests.write(str(number) + "; ")

        # Тест 5: присутствуют отрицательные числа
        if find_numbers_in_file("tests/input05.txt") == [21, 1983, -89.2, 13, 1922, 57.8]:
            tests.write("Test 5: passed.\n")
        else:
            tests.write("Test 5: failed.\n")
            for number in find_numbers_in_file("tests/input05.txt"):
                tests.write(str(number) + "; ")


# Проводим тесты
test_cases()

# Вывод результата
with open("output.txt", "w") as outputFile:
    for number in find_numbers_in_file("input.txt"):
        outputFile.write(str(number) + "; ")
