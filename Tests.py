import unittest
from main import find_numbers_in_file


class TestFindNumbers(unittest.TestCase):

    # Тест 1: в тексте только целые числа
    def test_first_case(self):
        expected_result = [20, 70, 50, 270]
        result = find_numbers_in_file("tests/input01.txt")
        self.assertEqual(result, expected_result)

    # Тест 2: только вещественные числа (с разделителем точка)
    def test_second_case(self):
        expected_result = [156.6, 13.01, 12.037, 56.9, 3.2, 182.08]
        result = find_numbers_in_file("tests/input02.txt")
        self.assertEqual(result, expected_result)

    # Тест 3: в файле есть вещественные числа (с разделителем запятая)
    def test_third_case(self):
        expected_result = [42.2, 6, 2.5, 140.5]
        result = find_numbers_in_file("tests/input03.txt")
        self.assertEqual(result, expected_result)

    # Тест 4: присутствуют вещественные числа с разными разделителями
    def test_fourth_case(self):
        expected_result = [30.27, 17.73]
        result = find_numbers_in_file("tests/input04.txt")
        self.assertEqual(result, expected_result)

    # Тест 5: присутствуют отрицательные числа
    def test_fifth_case(self):
        expected_result = [21, 1983, -89.2, 13, 1922, 57.8]
        result = find_numbers_in_file("tests/input05.txt")
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
