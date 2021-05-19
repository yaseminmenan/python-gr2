# Declararea unei liste
list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# Afisarea unei alte liste ordonate ascendent
print(sorted(list))

# Afisarea unei alte liste ordonate descendent
print(sorted(list, reverse=True))

# Afisarea numerelor pare din lista cu slice
even_sliced_list = list[1:4:2] + list[6:8:] + [list[9]]
print(even_sliced_list)

# Afisarea numerelor impare din lista cu slice
odd_sliced_list = list[0:3:2] + list[4:6:] + [list[8]]
print(odd_sliced_list)

# Afisarea elementelor multipli ai lui 3
for element in list:
    if element % 3 == 0:
        print(element, end=' ')
