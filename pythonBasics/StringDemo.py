str = 'RahulShettyAcademy.com'
str1 = 'Consulting Firm'
str3 = 'RahulShetty'

print(str[1])
print(str[0:5])     # substring in python

print(str+str1)    # Concatenation

print(str3 in str)    # substring check

var = str.split('.')
print(var)
print(var[0])

str4 = ' great '
print(str4.strip())   # remove left & right wide spaces

print(str4.lstrip())    # remove left wide spaces
print(str4.rstrip())    # remove right wide spaces
