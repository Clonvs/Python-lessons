# Семинар 4

# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# lst = [23, 45, 21, 22, 78, 153, 16]
# lst_length = len(lst)
# sum_elements = 0
# count = 1
# while count < lst_length:   
#    sum_elements = sum_elements + lst[count]
#    count = count + 2
# print(lst,'->',sum_elements)


# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

# import random 

# A = int(input('Введите количество строк: '))
# B = int(input('Введите количество столбцов: '))
# array = []
# for i in range(A):
#    array.append([])
#    for j in range(B):
#       array[i].append(random.randint(0, 100))   

# print('matrix:')
# for u in range(A):
#    print(array[u])


# for m in range(A):
#    s = 0
#    for n in range(B):
#       s+=array[m][n]         
#    print(s // 2,end=", ")


# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором

# from random import randint
# kol_elem = 30

# s = [randint(0, 30) for i in range(kol_elem)]
# print('Произвольный список -> ',s)
# for i in range(kol_elem - 1):
#    m = i
#    for j in range(i + 1, kol_elem):
#       if s[m] > s[j]:
#          m = j
#    s[i], s[m] = s[m], s[i]
# print('Отсортированный список -> ',s) 
