import pytest
from solution_valid_anagram import (
    SortedSolution,
    CounterSolution,
    HashMapSolution,
    OnlyOneHashMapSolution,
)


@pytest.fixture(
    params=[SortedSolution, CounterSolution, HashMapSolution, OnlyOneHashMapSolution]
)
def solution(request):
    return request.param()


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("racecar", "carrace", True),
        ("jar", "jam", False),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("lion", "lliioonn", False),
    ],
)
def test_is_anagram(solution, s, t, expected):
    assert solution.isAnagram(s, t) == expected
