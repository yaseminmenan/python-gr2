import copy
import random

# print('Curs 3!!!')

# elements = [x for x in range(11)]
# # print(choices)
# while True:
#     random_choice = random.choice(elements)
#     if random_choice % 3 == 0:
#         break
#     print(f'Random choice is {random_choice}')
#
# print(f'Exit random choice is {random_choice}')


# for i in range(11):
#     if i % 2 != 0:
#         continue
#     print(f'Numar par: {i}')

my_sum = 0


def get_sum(a, b):
    my_sum = a + b
    print(my_sum)


# get_sum(1, 2)
# print(my_sum)


# l1 = [1, 2, 3]
l1 = [1, 2, 3, [2, 3, 4]]

# l2 = l1 -> referinta
# l2 = l1.copy()
# l2 = copy.deepcopy(l1)
l2 = list(l1)
l2[3].append(5)
# l2 = [l1, 4]


# print(l1)
# print(l2)


# def my_function(nume, prenume, *args, **kwargs):
#     tail = ' '.join(args)
#     print(f'{nume} {prenume} {tail}')
#
#     for key in kwargs.keys():
#         print(f'key: {key} has value {kwargs[key]}')


# my_function('popescu', 'ana', 'are', '2', 'mere', job='developer', age=22)


# while True:
#     my_var = input('Introducteri un nr: ')
#     try:
#         my_int = int(my_var)
#         print(my_ints)
#     except ValueError as e:
#         print('Please enter a numeric value')
#     except NameError:
#         print('You have used an undefined var')
#         pass
#     else:
#         print('No exceptions occured')
#     finally:
#         print('We will print this if there\'s an exception or not')

# print(dir(__builtins__))

msg = 'coco'


def my_function():
    global msg
    msg = 'Hello World!'
    print(msg)


print(msg)
my_function()
print(msg)
