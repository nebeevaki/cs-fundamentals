from random import randint


def quick_sort(nums: list[int]) -> None:
    if not nums:
        return

    _quick_sort(nums, left=0, right=len(nums) - 1)


def _quick_sort(nums: list[int], left: int, right: int) -> None:
    """
    Делим отрезок на две части, сортируем каждый из них согласно правилам partition
    (выбирая опорный элемент и сортируя слева него все элементы меньше, справа все элементы больше него)
    """
    if left >= right:
        return

    equal, greater = _partition(nums, left, right) # получаем указатели на равное pivot и на первый больший pivot

    _quick_sort(nums, left, equal - 1) # сортируем первую половину
    _quick_sort(nums, greater, right) # сортируем вторую половину

def _partition(nums: list[int], left: int = 0, right: int | None = None) -> tuple[int, int]:
    """
    partition через три указателя.
    equal - указатель на первый индекс, равного pivot
    greater - указатель на первый индекс, большего pivot
    current - указатель на текущий индекс
    """
    if right is None:
        right = len(nums) - 1

    pivot = nums[randint(left, right)] # выбираем опорный элемент
    equal = greater = current = left # три указателя

    while current <= right: # до момента, пока не дойдем до правой границы
        if nums[current] > pivot: # если текущий элемент больше опорного, просто идем дальше
            current += 1
        elif nums[current] == pivot: # если равен опорному, то просто меняем его с greater и увеличиваем счетчики
            nums[greater], nums[current] = nums[current], nums[greater]
            greater += 1
            current += 1
        elif nums[current] < pivot: # если меньше опорного, меняем в greater, а после с equal
            nums[greater], nums[current] = nums[current], nums[greater]
            nums[equal], nums[greater] = nums[greater], nums[equal]
            equal += 1
            greater += 1
            current += 1
    return equal, greater
