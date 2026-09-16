from random import randint


def kth_largest(nums: list[int], k: int) -> int:
    """
    Найти k-й максимальный.
    Например, найти третий максимальный элемент в последовательности.
    """
    if not 1 <= k <= len(nums):
        raise IndexError("k is out of range")
    return _quickselect(nums=nums, k=len(nums) - k, left = 0, right=len(nums) - 1)

def kth_smallest(nums: list[int], k: int) -> int:
    """
    Найти k-й минимальный.
    Например, найти третий минимальный элемент в последовательности.
    """
    if not 1 <= k <= len(nums):
        raise IndexError("k is out of range")

    return _quickselect(nums=nums, k=k - 1, left=0, right=len(nums) - 1)


def _quickselect(nums: list[int], k: int, left: int, right: int) -> int:
    """
    На вход получаем последовательность чисел и k-ый индекс, который нам нужно найти.
    Через partition выбираем опорный элемент и смотрим в какой части у нас находится k-ый индекс относительно опоры.
    Двигаем границу до момента, пока не найдем, чему равен элемент под индексом k.
    """
    while left <= right:
        equal, greater = _partition(nums, left, right) # вызываем partition для текущих границ

        if k < equal: # если искомый элемент в левой части - двигаем правую границу
            right = equal - 1
        elif k >= greater: # если искомый элемент в правой части - двигаем левую границу
            left = greater
        else: # иначе элемент между equal, greater, значит мы его нашли
            return nums[k]

    raise RuntimeError("unreachable")


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
