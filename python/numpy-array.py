import numpy as np

nums = [ [1,2,3], [4,5,6]]

nums = np.array(nums)
# Print second row of nums
print(nums[1, :])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:, 2] + 1
print(nums)

# You have a list of guests (the names list). Each guest, for whatever reason,
# has decided to show up to the party in 10-minute increments. For example,
#  Jerry shows up to Festivus 10 minutes into the party's start time, Kramer shows up
#  20 minutes into the party, and so on and so forth.

# Create a list of arrival times
arrival_times = [*range(10,60,10)]
# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

names = ['Kramer', 'Elaine', 'George', 'Newman', 'Apo']
# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[index],time) for index,time in enumerate(new_times)]

print(guest_arrivals)

# ns	nanosecond	10-9
# µs (us)	microsecond	10-6
# ms	millisecond	10-3
# s	second	100