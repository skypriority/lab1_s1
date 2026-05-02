from typing import List, Tuple, Literal
import random
import unittest


def guess_number(
    target: int,
    numbers: List[int],
    method: Literal["linear", "binary"] = "linear"
) -> Tuple[int, int]:

    if method == "linear":
        attempts = 0
        for num in numbers:
            attempts += 1
            if num == target:
                return num, attempts
        raise ValueError("Number not found in list")

    elif method == "binary":
        sorted_numbers = sorted(numbers)
        low, high = 0, len(sorted_numbers) - 1
        attempts = 0
        while low <= high:
            attempts += 1
            mid = (low + high) // 2
            guess = sorted_numbers[mid]
            if guess == target:
                return guess, attempts
            elif guess < target:
                low = mid + 1
            else:
                high = mid - 1
        raise ValueError("Number not found in list")

    else:
        raise ValueError("Invalid search method")


def input_values() -> Tuple[int, List[int]]:

    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    numbers = list(range(start, end + 1))
    target = random.choice(numbers)
    return target, numbers


class TestGuessNumber(unittest.TestCase):
    def setUp(self):
        self.numbers = list(range(1, 11))

    def test_linear_search_found(self):
        target = 7
        found, attempts = guess_number(target, self.numbers, "linear")
        self.assertEqual(found, target)
        self.assertEqual(attempts, 7)

    def test_binary_search_found(self):
        target = 7
        found, attempts = guess_number(target, self.numbers, "binary")
        self.assertEqual(found, target)
        self.assertLessEqual(attempts, len(self.numbers).bit_length())

    def test_number_not_found(self):
        with self.assertRaises(ValueError):
            guess_number(100, self.numbers, "linear")

    def test_invalid_method(self):
        with self.assertRaises(ValueError):
            guess_number(5, self.numbers, "unknown")


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
