a: int = 5
b: str = 'строка'
c: list = [1, 2]

print(a, "относится к типу", type(a))

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s
print(indent('69', 69))

def string_length(s: str = '') -> int:
    return len(s)

def min_list(e: list, r: list) -> int:
    return max(len(e), len(r))

def append_list(my_list: list):
    my_list.append('test')
    return my_list

print(append_list([1,2,4]))

def sum_list(my_list: list) -> int:
    result = 0
    for elem in my_list:
        result = result + elem
    return result

print(sum_list([1,2,3]))