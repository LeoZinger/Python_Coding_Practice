
from heapq import heapify, heappush, heappop
a = [1, 2, 3]
print(a[-3])
print(a[-2])
print(a[-1])
##########################
subjects = ('Python', 'Interview', 'Questions')
for i, subject in enumerate(subjects):
    print(i, subject)

##########################
globvar = 0
def set_globvar_to_one():
    global globvar  # Needed to modify global copy of globvar
    globvar = 1

set_globvar_to_one()
print(globvar)
#########################
list1 = [1, 3, 2]
print(list1 * 2)
#########################
print(list("hello"))
#########################
a = [1,2,3,4,5]
avg = 0
total = 0
for i in a:
    total += i
print("avg="+str(total/len(a)))
#########################
print([x for x in range(1,26) if x%5!=0])
print(list(filter(lambda x:x%5!=0, range(1,26))))
#########################
#reverse a number
#num=int(input("Enter number: "))
num = 12345
#a = num // 10
b = 0
while num > 0:
    a = num // 10
    print(a)
    r = num % 10
    print(r)
    b = b * 10 + r
    num = num // 10
print("The reverse of the number:", b)
#########################
# read/write from a file
L = [ 'Python \n', 'is \n', 'an \n','awesome \n','language \n']
with open("testfile.txt", "w") as file1:
    file1.write("Hello \n")
    file1.writelines(L)
with open("testfile.txt", "r+") as file1:
    # Reading form a file
    print(file1.read())
#########################
#count the vowels in a str
str1 = "I am a string with vowels in it"
vowels = [x for x in str1 if x in ('a', 'e', 'i', 'o', 'u')]
print("Total number of vowels in the string is ", len(vowels))
#check if string is palindrome
#str1 = "totot"
#str1=raw_input("Enter string:")
a = list(str1)
print("str a = ", a)
b = a[:]
b.reverse()
print("after reverse\nstr a = ", a)
print("str b = ", b)
if str1 == str1[::-1]:
    print (str1, " is a palindrome")
else:
    print(str1, " is NOT a palindrome")
#####################################
# swap first and last value of a list
a = [1,2,3,4,5]
print(a)
temp = a[0]
print("temp=", temp, " a[0]=", a[0])
a[0] = a[-1]
print("a[-1]=", a[-1])
a[-1] = temp
print(a)
#######################
#Write Python Program to Find the Second Largest Number in a List:
a = [1,2,3,4,5]
#n = int(input("Enter the number of integer elements : "))
# for i in range(n):
#     int_element = int(input("Enter " + str(i+1)
#                             + "th integer element : "))
#     a.append(int_element)
print("list = ", a)
# heap = [float('inf')]*2
# heapify(heap)
# for i in a:
#     heappush(heap, -i)
# second_max = heappop(heap)
# second_max = heappop(heap) * -1
max_int = float('-inf')
second_max_int = float('-inf')
print("second_max_int = ", second_max_int)
for i in a:
    if i > max_int:
        second_max_int = max_int
        max_int = i
        print("second_max_int = ", second_max_int)
    elif i > second_max_int:
        second_max_int = i
print("final: second_max_int = ", second_max_int)
#########################
# check if a number is Armstrong number
n=input("Enter any number: ")
a=list(map(int,n))
print("a=", a)
b=list(map(lambda x:x**3,a))
print("b=", b)
if(sum(b)==int(n)):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")
#########################



