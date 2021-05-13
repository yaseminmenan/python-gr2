print('Acesta este cursul al 2-lea!')

name = "Ana"

if name:
    print(name)
    print(type(name))
    print(3 ** 2)
else:
    print(names)  # this is an inline comment
    print("Nu avem niciun nume")

first_person = {'Name': 'John'}
second_person = {'Name': 'John'}
# second_person = first_person

if first_person is second_person:
    print('they are the same')
else:
    print('they are NOT the same')

if first_person == second_person:
    print('they are the same')
else:
    print('they are NOT the same')

my_str = "Ana are mere"
print(my_str[2])
# my_str[2] = 'b'

print(ord('a'))
print(chr(10))  # newline

another_str = 'Owner\'s \n\tmanual'
print(another_str)

msg = "{} has {} years".format('Ion', 18)
print(msg)

name = 'Ion'
age = 18
msg_2 = f"{name} has {age+2} years"
print(msg_2)

l = [1, 2, 3, 'Ana are mere', True, False, None, [4, 5, 6]]
print(l[2])
l[2] = '99'
print(l[2])

inventar = ["faina", "drojdie", "apa", "sare"]

for item in inventar:
    print(item)

for index, value in enumerate(inventar):
    print(f'{value} la pozitia {index}')

print(inventar[-1])
print(inventar[len(inventar) - 1])
print(inventar[-4])

list1 = [2, 3, 0, 9]
list1.sort()
print(list1)
list2 = [2, 3, 0, 9]
print(sorted(list2))

l1 = [2, 3, 0, 9]
l2 = [12, 13, 10, 9]
l3 = l1 + l2
l1 = l1 + l2
print(l1)

my_dict = {1: "Home", 2:"Office", 3: "Restaurant"}
for key, val in my_dict.items():
    print(f'{key} => {val}')

print(my_dict[3])

print(my_dict.get(2, 'Nu exista cheia'))
print(my_dict.get(22, 'Nu exista cheia'))

v = my_dict.get(4, '**')
print(v)

l1 = [1, 2, 2, 3]
l2 = [1, 9, 2, 0]
print(l)

s1 = set(l1)
s2 = set(l2)

print(list(s1.intersection(s2)))
print(list(s1 | s2))
print(list(s1 & s2))