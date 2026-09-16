import pytest
from quick_sort import quick_sort

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
    ],
)
def test_quick_sort(nums: list[int]) -> None:
    expected = sorted(nums)

    quick_sort(nums)

    assert nums == expected
