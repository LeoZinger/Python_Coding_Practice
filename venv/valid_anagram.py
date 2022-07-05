from collections import Counter
def valid_anagram(s, t):
    n = len(s)
    m = len(t)
    print((list(s)))
    sc = Counter((list(s)))
    print(sc)
    tc = Counter((list(t)))
    print(tc)
    return sc == tc


s = "dog"
t = "god"
print("valid anagram?", valid_anagram(s,t))

# will return a itertools chain object
# which is basically a pseudo iterable container whose
# elements can be used when called with a iterable tool
print(Counter(['a', 'b', 'c', 'a', 'b', 'b']))

s = {"a":5, "b":3, "c":1}
for k, v in enumerate(s):
    print(k, "=", v)