# expected output {65: 'A', 66: 'B', 67: 'C', 68: 'D'}
ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

new_dict = {}
# for char in ascii_dict.keys():
#     new_dict[ascii_dict[char]] = char

# Reverse mapping
new_dict = {value: key for key, value in ascii_dict.items()}

print(new_dict)