#Задача №1
def task_1() -> str:
    a: int = 4
    b: float = 5.5
    c: str = 'строка'
    d: list = [3, 4]
    e: bool = True
    return type(a), type(b), type(c), type(d), type(e)
    #
    # print(a, "относится к типу", type(a))
    # print(b, "относится к типу", type(b))
    # print(c, "относится к типу", type(c))
    # print(d, "относится к типу", type(d))
    # print(e, "относится к типу", type(e))

print(task_1())

#Задача №2
# последовательность Фибоначчи
def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]
    # print(a[0:3])
print(task_2())


#Задача №3
def task_3(qw: int) -> int:
    return qw * qw

print(task_3(9))