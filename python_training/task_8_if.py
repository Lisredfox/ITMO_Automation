# Программа проверяет является число положительным
# или отрицательным и выводит соотвествующее сообщение.

# num = 3

# Также попробуйте следующие варианты значения num.
num = -5
# num = 0

if num >= 0:
    print('Число больше или равно 0')
else:
    print('Число отрицательное')


def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print("YES")
    else:
        print("NO")

task_yes_no(str_1='test', str_2='test1')


#num_float = 3.4
# Также попробуйте варианты
#num_float = 0
num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательно')


permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

# def task_kurs(num_kurs: int):
#     if num_kurs >= 1 and num_kurs <= 4:
#         print("Бакалавр")
#     elif num_kurs >= 5 and num_kurs <= 6:
#         print("Магистр")
#     elif num_kurs >= 7 and num_kurs <= 9:
#         print('Асспирант')
#     else:
#         print("Введите корректный год обучения")
#
# task_kurs(8)

def student_rank(year_of_study):
    if year_of_study == 1 or year_of_study == 2 or year_of_study == 3 or year_of_study == 4:
        print('Вы - бакалавр')
    elif year_of_study in range(5, 7):
        print('Вы - магистр')
    elif 7 <= year_of_study <=9:
        print('Вы - аспирант')
    else:
        print('Введите корректный год обучения')

student_rank(5)


num = 5

if num > 100 or num < -100:
    print("-")
else:
    print("+")