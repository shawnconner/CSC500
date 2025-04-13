import array


my_array = array.array('i', [92, 94, 96, 98])

for i in range(0, len(my_array)):
    print("Grade  ", i, ": ", my_array[i])

print(min(my_array))
print(max(my_array))