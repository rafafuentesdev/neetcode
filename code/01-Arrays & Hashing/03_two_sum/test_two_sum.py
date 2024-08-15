import pytest
from solution_two_sum import BruteForceSolution, OptimizedSolution


@pytest.fixture(
    params=[
        BruteForceSolution,
        OptimizedSolution,
    ]
)
def solution(request):
    return request.param()


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([3, 4, 5, 6], 7, [0, 1]),
        ([4, 5, 6], 10, [0, 2]),
        ([5, 5], 10, [0, 1]),
    ],
)
def test_two_sum(solution, nums, target, expected):
    assert solution.twoSum(nums, target) == expected
