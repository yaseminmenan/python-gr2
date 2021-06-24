# Declararea unei liste
list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(list)

# Afisarea unei alte liste ordonate ascendent
print(sorted(list))

# Afisarea unei alte liste ordonate descendent
print(sorted(list, reverse=True))

# Afisarea numerelor pare din lista cu slice
sorted_list = sorted(list)
# even_sliced_list = list[1:4:2] + list[6:8:] + [list[9]]
even_sliced_list = sorted_list[1::2]
print(even_sliced_list)

# Afisarea numerelor impare din lista cu slice
#odd_sliced_list = list[0:3:2] + list[4:6:] + [list[8]]
odd_sliced_list = sorted_list[::2]
print(odd_sliced_list)

# Afisarea elementelor multipli ai lui 3
multipli = [x for x in list if x % 3 == 0]
print(multipli)
