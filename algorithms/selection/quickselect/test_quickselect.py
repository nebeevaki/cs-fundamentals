from random import Random

import pytest

from algorithms.selection.quickselect.quick_select import kth_smallest, kth_largest


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([7, 2, 9, 1, 5, 3], 1, 1),
        ([7, 2, 9, 1, 5, 3], 3, 3),
        ([7, 2, 9, 1, 5, 3], 6, 9),
        ([42], 1, 42),
        ([-5, -10, 0, 3, -1], 1, -10),
        ([5, 5, 5, 5], 3, 5),
        ([3, 1, 3, 2, 3], 3, 3),
    ],
)
def test_kth_smallest(
    nums: list[int],
    k: int,
    expected: int,
) -> None:
    assert kth_smallest(nums, k) == expected


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([7, 2, 9, 1, 5, 3], 1, 9),
        ([7, 2, 9, 1, 5, 3], 3, 5),
        ([7, 2, 9, 1, 5, 3], 6, 1),
        ([42], 1, 42),
        ([-5, -10, 0, 3, -1], 1, 3),
        ([5, 5, 5, 5], 2, 5),
        ([3, 1, 3, 2, 3], 2, 3),
    ],
)
def test_kth_largest(
    nums: list[int],
    k: int,
    expected: int,
) -> None:
    assert kth_largest(nums, k) == expected


@pytest.mark.parametrize("k", [0, -1, 6, 100])
def test_kth_smallest_invalid_k(k: int) -> None:
    nums = [1, 2, 3, 4, 5]

    with pytest.raises(IndexError):
        kth_smallest(nums, k)


@pytest.mark.parametrize("k", [0, -1, 6, 100])
def test_kth_largest_invalid_k(k: int) -> None:
    nums = [1, 2, 3, 4, 5]

    with pytest.raises(IndexError):
        kth_largest(nums, k)


def test_random_arrays() -> None:
    random = Random(42)

    for _ in range(100):
        nums = [
            random.randint(-1000, 1000)
            for _ in range(100)
        ]

        k = random.randint(1, len(nums))

        assert (
            kth_smallest(nums.copy(), k)
            == sorted(nums)[k - 1]
        )

        assert (
            kth_largest(nums.copy(), k)
            == sorted(nums, reverse=True)[k - 1]
        )