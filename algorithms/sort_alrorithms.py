import unittest


def insert_sort(arr: list):
    """Sort by insertion"""
    for i in range(1, len(arr)):
        item_to_insert = arr[i]
        j = i - 1
        while j >= 0 and item_to_insert < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = item_to_insert


def insert_sort_v2(arr):
    """Sort by insertion V2"""
    for i in range(1, len(arr)):
        k = i
        while k > 0 and arr[k-1] > arr[k]:
            arr[k-1], arr[k] = arr[k], arr[k-1]
            k -= 1


def choice_sort(arr):
    """Choice sort"""
    n = len(arr)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if arr[k] < arr[pos]:
                arr[k], arr[pos] = arr[pos], arr[k]


def bubble_sort(arr):
    """Bubble sort"""
    n = len(arr)
    for bypass in range(1, n):
        for k in range(0, n-bypass):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]


class TestSortAlgorithm(unittest.TestCase):
    def setUp(self) -> None:
        self.sort_functions = [insert_sort, insert_sort_v2, choice_sort, bubble_sort]

    def test_case_one(self):
        """Test Case 1"""
        sorted_list = [1, 2, 3, 4, 5]
        for sort_function in self.sort_functions:
            with self.subTest(function=sort_function.__doc__):
                list_ = [4, 2, 1, 3, 5]
                sort_function(list_)
                self.assertSequenceEqual(list_, sorted_list)

    def test_case_two(self):
        """Test Case 2"""

        sorted_list = list(range(20))
        for sort_function in self.sort_functions:
            with self.subTest(function=sort_function.__doc__):
                list_ = list(range(10, 20)) + list(range(10))
                sort_function(list_)
                self.assertSequenceEqual(list_, sorted_list)

    def test_case_three(self):
        """Test Case 3"""
        sorted_list = [1, 2, 2, 4, 4]
        for sort_function in self.sort_functions:
            with self.subTest(function=sort_function.__doc__):
                list_ = [4, 4, 2, 1, 2]
                sort_function(list_)
                self.assertSequenceEqual(list_, sorted_list)


if __name__ == "__main__":
    unittest.main()

