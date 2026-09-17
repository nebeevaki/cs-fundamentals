import random
import pytest

from algorithms.sorting.merge_sort.merge_sort import merge_sort


@pytest.mark.parametrize(
    "nums",
    [
        [5, 3, 8, 1, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [5, 2, 5, 1, 5, 2],
        [-3, 5, -1, 0, -10],
        [42],
        [],
    ]
)
def test_merge_sort(nums: list[int]) -> None:
    expected = sorted(nums)
    sorted_nums = merge_sort(nums)
    assert sorted_nums == expected


def test_merge_sort_random():
    for _ in range(100):
        nums = [
            random.randint(-1000, 1000)
            for _ in range(random.randint(0, 100))
        ]

        expected = sorted(nums)
        sorted_nums = merge_sort(nums)

        assert sorted_nums == expected