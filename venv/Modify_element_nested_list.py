list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
# Change the element 35 to 3500
# Expected Output: -
# [5, [10, 15, [20, 25, [30, 3500], 40], 45], 50]

# def iter_nest_list(list):
#     for i in list:
#         if i == 35:
#             list.remove(i)
#             list.append(3500)
#         if type(i) == type([]):
#             iter_nest_list(i):

list1[1][2][2][1] = 3500
print(list1)

