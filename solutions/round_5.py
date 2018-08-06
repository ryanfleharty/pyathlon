my_list = [1,2,3,4,5]
for index in range(len(my_list)):
    my_list[index] = my_list[index] * 2
print(my_list)


# a for loop wont access/change the underlying array,
# so you have to loop over the indexes using range(len(list))
# and use the index to directly re-assign the values in the array
