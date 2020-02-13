import numpy as np

mynumber = 1
myfloat = 3.14

mystring = 'Hello World!'
myboolean = True
mylist = [1, 2, 3, 4, 5]

print(mynumber)
print(myfloat)
print(mystring)
print(myboolean)
print(mylist)

print(f'{type(mynumber)}, {type(myfloat)}, {type(mystring)}, {type(myboolean)}, {type(mylist)}')

mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def double(mylist1):
    return [x * 2 for x in mylist1]
print(double(mylist1[4:7]))

def split(mylist1):
    even_list = []
    odd_list = []
    for x in mylist1:
        if (x % 2 == 0):
            even_list.append(x)
        else:
            odd_list.append(x)
    print("Even lists:", even_list)
    print("Odd lists:", odd_list)
print(split(mylist1))

for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
