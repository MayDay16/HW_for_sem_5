# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
import random

def task_1():
    size = 10
    more_than = 5
    numbers = [random.randint(1,10) for i in range (size)]
    print(f'Cписок случайных чисел от 1 до 10: {numbers}')
    numbers = list(filter(lambda x: x>more_than,numbers))
    print(f'Элементы которые больше чем {more_than}: {numbers}')
    print()
task_1()

# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def task_2(user_list):
    
    random_list = []
    random_list.append(user_list[0])
    for i in range(len(user_list)):
        if user_list[i] in random_list:
            continue
        elif user_list[i] > user_list[0] and user_list[i] > random_list[len(random_list)-1]:
            random_list.append(user_list[i])
    return random_list

size = 20
random_list = list(random.randint(1, 30) for i in range(size))
print(f'Случайный список: {random_list}')

result = (f'Случайная возрастающая последовательность: {task_2(random_list)}') 
print(result)
print()

# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаютСписок уникальных элементов
# [1, 4, 2, 3, 6, 7]

def task_3():
    size = 10
    random_list = list(random.randint(1, 10) for i in range(size))
    print(f'Cписок случайных чисел от 1 до 10: {random_list}')

    same = list(map(lambda x: list.count(random_list, x) > 1, random_list)).count(True)


    print(f'Количество совпадающих элементов: {same}')

    print(f"Список уникальных элементов {list(set(random_list))}")
    print()
task_3()

# Задача 4*. Создайте игру в крестики-нолики.