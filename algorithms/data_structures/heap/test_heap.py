import random

import pytest

from algorithms.data_structures.heap.heap import Heap


def test_add() -> None:
    heap = Heap()

    for num in [5, 3, 8, 1, 2]:
        heap.add(num)

    assert heap.peek() == 1
    assert len(heap) == 5


@pytest.mark.parametrize(
    "nums",
    [
        [5, 3, 8, 1, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [5, 2, 5, 1, 5, 2],
        [-3, 5, -1, 0, -10],
        [42],
    ],
)
def test_pop(nums: list[int]) -> None:
    heap = Heap()

    for num in nums:
        heap.add(num)

    result = []

    while len(heap) > 0:
        result.append(heap.pop())

    assert result == sorted(nums)


def test_duplicates() -> None:
    heap = Heap()

    nums = [5, 5, 1, 1, 3, 3, 1]

    for num in nums:
        heap.add(num)

    result = []

    while len(heap) > 0:
        result.append(heap.pop())

    assert result == sorted(nums)


def test_negative_numbers() -> None:
    heap = Heap()

    nums = [-5, -1, -10, 0, 3, -3]

    for num in nums:
        heap.add(num)

    result = []

    while len(heap) > 0:
        result.append(heap.pop())

    assert result == sorted(nums)


def test_peak_does_not_remove_element() -> None:
    heap = Heap()

    heap.add(3)
    heap.add(1)
    heap.add(2)

    length_before = len(heap)

    assert heap.peek() == 1
    assert len(heap) == length_before


def test_pop_empty_heap() -> None:
    heap = Heap()

    with pytest.raises(IndexError):
        heap.pop()


def test_len() -> None:
    heap = Heap()

    assert len(heap) == 0

    heap.add(5)
    heap.add(1)

    assert len(heap) == 2

    heap.pop()

    assert len(heap) == 1


def test_random() -> None:
    random.seed(42)

    nums = [random.randint(-1000, 1000) for _ in range(1000)]

    heap = Heap()

    for num in nums:
        heap.add(num)

    result = []

    while len(heap) > 0:
        result.append(heap.pop())

    assert result == sorted(nums)
