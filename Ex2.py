my_list = [1, 4, 2, 4, 5, 6, 7, 1, 6, 9, 9, 9, 10]
duplicate = set()
for elem in my_list:
    if my_list.count(elem) == 2:
        duplicate.add(elem)
duplicate_list = list(duplicate)
print(duplicate_list)
