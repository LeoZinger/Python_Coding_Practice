# Remove numbers greater than 50
number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print([x for x in number_list if x <= 50])
# number_list.sort()
print(number_list)
for i in range(len(number_list)-1, -1, -1):
    if number_list[i] > 50:
        # number_list = number_list[:i]
        del number_list[i]
print(number_list)