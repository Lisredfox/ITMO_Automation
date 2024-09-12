# Задача №1
a = 15
b = 82
if a > b:
    print(a)
else:
    print(b)

# Задача №2
def task_step_135(num_1: int, num_2: int):
    num_3 = abs(num_1 - num_2)
    if num_3 == 135:
        print('Yes')
    else:
        print('No')

task_step_135(0, 135)

# Задача №3
def task_season(num_month: int) -> str:
    if num_month == 12 or num_month == 1 or num_month == 2:
        print('зима')
    elif  3 <= num_month <=5:
        print('весна')
    elif 6 <= num_month <= 8:
        print ('лето')
    elif 9 <= num_month <=11:
        print('осень')
    else:
        print('Неправильное число. Введите номер месяца от 1 до 12.')

task_season(9)

# Задача №4
def task_num_three(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')

task_num_three(11,15,20)

# Задача №5
def task_list_positive(nums = []):
    positive = 0
    for num in nums:
        if num > 0:
            positive +=1
    print(positive)

task_list_positive([1, -5, -9, 2, 4])

# Задача №6
def task_sum_days (years: int, months:int):
    days = (years * 365 + months * 29)
    print(days)

task_sum_days(1, 1)