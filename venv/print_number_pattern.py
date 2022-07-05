# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

n = 5
x= 0
for i in range(n):
    x = i + 1
    for j in range(n-i):
        print(x, end=' ')
    print("\n")