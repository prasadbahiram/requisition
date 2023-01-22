print('hello')

a = 3
print(a)
str = 'Hello World'
print(str)

b,c,d = 3,4.5,'Aaba'
print(b, c, d)

print('{}{}'.format('Value is ',b))

print(type(b))
print(type(c))
print(type(d))

# List
values = [1, 2, 'Vaishali', 3.5, 7]
print(values)

print(values[0])
print(values[2])
print(values[-1])
print(values[1:4])

values[2] = 'VAISHALI'    # Upadte name in the list
print(values)

del values[4]     # delete array in the list
print(values)

# Tuple - same as List data type but immutable
val = (3, 5, 'Bahiram', 6.5, 8)
print(val)
print(val[0])
#val[2] = 'BAHIRAM'
#print(val)

#del val[4]
#print(val)

# Dictionary
dict = {1:'Vaishali','a':576}
print(dict['a'])
print(dict[1])

dict = {}
dict['LastName'] = 'Bahiram'
dict[2] = 'Anu'
dict['b'] = 999
print(dict)
