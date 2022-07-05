def reverStr(str):
    n = len(str)
    if not n or n == 0:
        return ""
    s = list(str)
    print(s)
    i = 0
    j = n-1-i
    while i < j:
        j = n-1-i
        t = s[i]
        s[i] = s[j]
        s[j] = t
        i += 1
        j -= 1
        print("i = ", i, s)
    return ''.join(s)
    # return ''.join(s[::-1])


str = "TestStr"
print(reverStr(str))