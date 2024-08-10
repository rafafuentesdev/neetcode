import pytest
from solution import (
    BruteForceSolution,
    SortingSolution,
    HashSetSolution,
    ConciseSetSolution,
)


@pytest.fixture(
    params=[BruteForceSolution, SortingSolution, HashSetSolution, ConciseSetSolution]
)
def solution(request):
    return request.param()


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ([1, 2, 3, 3], True),
        ([1, 2, 3, 4], False),
        ([1], False),
        ([], False),
        ([1, 1, 1, 1], True),
    ],
)
def test_contains_duplicate(solution, input_data, expected):
    assert solution.containsDuplicate(input_data) == expected
