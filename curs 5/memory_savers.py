import copy

print('Curs 5 - Memory Savers')
print('-' * 80)

my_lambda = lambda x, y: x + y
my_sum = my_lambda(2, 3)
print(my_sum)
print()

players = [
    {
        'first name': 'John',
        'last name': 'Doe',
        'rank': 3
    },
    {
        'first name': 'Kevin',
        'last name': 'McDonald',
        'rank': 8
    },
    {
        'first name': 'Brad',
        'last name': 'Kelvin',
        'rank': 2
    }
]
print(players)
sorted_players = sorted(players, key=lambda player: player['rank'])
print(sorted_players)
print()

# map


def check_top_3_player(player):
    updated_player = copy.deepcopy(player)
    updated_player['is_top_three'] = True if player['rank'] <= 3 else False
    return updated_player


top_players_map = map(check_top_3_player, players)  # iterabil de tip map
top_players = list(top_players_map)
print(top_players)
print()

# filter

all_mcdonalds = list(filter(lambda player: player['last name'] == 'McDonald', players))
print(all_mcdonalds)
print()

# zip

letters = ['a', 'b', 'c', 'z']
numbers = [1, 2, 3]
print(zip(letters, numbers))  # iterabil zip
for tuple in zip(letters, numbers):
    print(tuple)
print()
for lit, nr in zip(letters, numbers):
    print(nr, lit)
print()
# list comprehension

my_numbers = [1, 2, 3, 4, 5]
squared_numbers = [item ** 2 for item in my_numbers if item % 2 == 0]
print(squared_numbers)