import pytest
from solution import Solution


@pytest.fixture
def solution():
    return Solution()


def test_contains_duplicate_example1(solution):
    assert solution.containsDuplicate([1, 2, 3, 3]) == True


def test_contains_duplicate_example2(solution):
    assert solution.containsDuplicate([1, 2, 3, 4]) == False


def test_contains_duplicate_empty_list(solution):
    assert solution.containsDuplicate([]) == False


def test_contains_duplicate_single_element(solution):
    assert solution.containsDuplicate([1]) == False


def test_contains_duplicate_all_same(solution):
    assert solution.containsDuplicate([2, 2, 2, 2]) == True


def test_contains_duplicate_negative_numbers(solution):
    assert solution.containsDuplicate([-1, -2, -3, -1]) == True


def test_contains_duplicate_mixed_numbers(solution):
    assert solution.containsDuplicate([1, -1, 2, -2, 3, -3]) == False
