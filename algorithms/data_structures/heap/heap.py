class Heap:
    def __init__(self):
        self.lst = []

    def add(self, x: int) -> None:
        """
        Добавляем новый элемент в кучу.
        Добавление в самый низ кучи, далее просеивание вверх, если родительский элемент больше - меняем два элемента.
        """
        self.lst.append(x)
        now_i = len(self.lst) - 1 # индекс нового добавленного элемента
        parent = (now_i - 1) // 2 # индекс родителя
        while now_i != 0 and self.lst[parent] > self.lst[now_i]: # пока не дошли до корня и родительский элемент больше
            self.lst[parent], self.lst[now_i] = self.lst[now_i], self.lst[parent] # меняем элементы местами
            now_i = parent # меняем индексы на новые
            parent = (now_i - 1) // 2

    def pop(self) -> int:
        if len(self.lst) == 0: # краевой случай пустой кучи
            raise IndexError("Heap пуст, невозможно взять элемент.")
        if len(self.lst) == 1: # краевой случай кучи с одним элементом
            return self.lst.pop()

        result = self.lst[0] # запоминаем минимальный элемент кучи для будущего возврата
        self.lst[0] = self.lst.pop() # переносим последний элемент кучи в верх
        now_i = 0 # ставим указатель на текущий индекс
        while True:
            left = (now_i * 2) + 1
            right = (now_i * 2) + 2
            if left >= len(self.lst): # случай, когда детей нет
                break
            if right >= len(self.lst): # правого ребенка нет, значит есть только левый
                if self.lst[now_i] > self.lst[left]: # в случае, если левый ребенок меньше текущего - меняем их местами
                    self.lst[now_i], self.lst[left] = self.lst[left], self.lst[now_i]
                break
            # проверка нужно ли менять текущий элемент с одним из детей(наименьшим)
            if self.lst[now_i] > self.lst[left] and self.lst[left] <= self.lst[right]: # случай, когда меняем с левым
                self.lst[now_i], self.lst[left] = self.lst[left], self.lst[now_i]
                now_i = left
            elif self.lst[now_i] > self.lst[right] and self.lst[right] < self.lst[left]: # случай, когда меняем с правым
                self.lst[now_i], self.lst[right] = self.lst[right], self.lst[now_i]
                now_i = right
            else: # текущий элемент уже меньше или равен обоим детям
                break

        return result


    def peek(self) -> int:
        if len(self.lst) == 0: # краевой случай пустой кучи
            raise IndexError("Heap пуст, невозможно посмотреть элемент.")
        return self.lst[0]


    def __str__(self) -> str:
        return str(self.lst)


    def __len__(self) -> int:
        return len(self.lst)
