numbers = {1, 2, 3, 4, 5}
doubled_numbers = [x*2 for x in numbers]
print(doubled_numbers)

names = {'Kramer', 'Elaine', 'George', 'Newman', 'Apo'} # or ['', '']..
# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)