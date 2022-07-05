# Display all duplicate items from a list
import collections

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80, 20, 20]
str = [str(x) for x in sample_list]
my_list = [int(x) for x in str]

dups = []
my_dict = {}

for i, count in collections.Counter(sample_list).items():
    if count > 1:
        dups.append(i)
# for i in my_list:
#     if i in my_dict and my_dict[i] == 1:
#         my_dict[i] = my_dict.get(i) + 1
#         dups.append(i)
#     else:
#         my_dict[i] = 1
print(dups)

