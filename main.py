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


# Вывод результата
with open("output.txt", "w") as outputFile:
    for number in find_numbers_in_file("input.txt"):
        outputFile.write(str(number) + " ")
