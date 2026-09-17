def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1: # базовый случай, в случае, если остался один элемент - возвращаем его
        return nums
    m = len(nums) // 2 # ищем середину списка и делим его на две части
    left = nums[:m]
    right = nums[m:]
    return _merge(merge_sort(left), merge_sort(right)) # рекурсивно вызываем слияние для двух наших частей

def _merge(left: list[int], right: list[int]) -> list[int]:
    i = j = 0 # два указателя для двух списков
    result = [] # итоговый список, который будет возвращен

    while i + j < len(left) + len(right): # выполнение, пока не пройдем до конца двух списков
        # если первый не закончился и (если второй закончился или элемент первого <= элементу второго)
        if i < len(left) and (j >= len(right) or left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result
