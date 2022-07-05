# expected result new dict {'A': 65, 'C': 67, 'F': 70}
# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
# Filter dict using following keys
l1 = ['A', 'C', 'F']

# new_dict = {}
# for c in l1:
#     if c in d1.keys():
#         print(c,":", d1[c])
#         new_dict[c] = d1[c]

new_dict = {key:d1[key] for key in l1}
print(new_dict)