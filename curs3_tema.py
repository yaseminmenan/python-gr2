from tema3_pkg import *


def your_function(*args, **kwargs):
    sum = 0
    for i in args:
        check_int = isinstance(i, int)
        check_float = isinstance(i, float)
        if check_int or check_float:
            sum += i
    return sum


def input_function():
    x = input()
    try:
        int(x)
    except ValueError:
        return 0
    else:
        return int(x)


print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc', param_1=2))

# print(input_function())

print(get_sum(3))
print(get_even_sum(3))
print(get_odd_sum(3))