# Create an outer function that will accept two strings, x and y. (x= 'Emma' and y = 'Kelly'.
# Create an inner function inside an outer function that will concatenate x and y.
# At last, an outer function will join the word 'developer' to it.

def outer(x,y):
    def inner(x,y):
        return x+y

    z = inner(x, y)
    return z + "Developer"

x = 'Emma'
y = 'Kelly'
print(outer(x,y))
