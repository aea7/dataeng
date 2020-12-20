# range
nums = range(0,10)
nums = list(nums)
print(nums)

print(list(range(0,11,2))) # equals to following
nums_list2 = [*range(0,11,2)]
print(nums_list2)

# enumerate

names = {'Kramer', 'Elaine', 'George', 'Newman', 'Apo'} # or ['', '']..
    # Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, start=1)]
print(indexed_names_unpack)

# map

names_map  = map(str.upper, names)
print(type(names_map))
names_uppercase = [*names_map]
print(names_uppercase)