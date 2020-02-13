# Reach part of homework 4
try:
    f = open('housing.data')
    print ('I have a file to process')
    f.close()
except FileNotFoundError:
    print('Boo, no file for me')

file = open('housing.data', 'r')
for lines in file:
    print(lines)
print (list(lines))