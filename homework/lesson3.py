# Семинар 3


# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.

# decimal = int(input('Введите десятичное число : '))
# s = ''
# alp = 'ABCDEF'
# while decimal > 0:
#     num = decimal % 16
#     if num < 10:
#         s = str(num) + s
#     else:
#         s = alp[num - 10] + s
#     decimal //= 16
# print(f'шестнадцатиричное число: {s}')


# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

# string = input()
# if '.' in string:
#     print('yes')
# else:
#     print('no')

# 3.12 Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку между первой и последней буквой "о" из исходной строки. Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.

# word = input('Введите слово: ')

# if word.count('о') >= 2:
#    index = word.find('о')
#    index1 = word.rfind('о')
#    string = word[:index + 1] + word[index1 - 1: index: - 1] + word[index1:]
#    print(string) 
# else:
#    print('Буквы "о" не найдено или она одна')     
     