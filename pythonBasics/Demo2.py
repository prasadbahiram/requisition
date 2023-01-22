
values = [1, 2, "Vaishali", 3.5, 7]

print(values[0])
print(values[3])
print(values[-1])
print(values[1:4])
values.insert(3,"Nikam")
print(values)
values.append("End")
print(values)
values[2] = "VAISHALI"
print(values)
del values[0]
print(values)

# Tuple - same as List data type but immutable
#val = (11, 12, "Vaishali", 13.5, 17)
#print(val[1])
#val[2] = "VAISHALI"
#print(val)

# Dictionary
dict = {"a":"Vaishali","b":"Nikam","c":66,4:77}
print(dict["a"])
print(dict[4])

#
dic = {}
dic["FirstName"] = "Vaishali"
dic["LastName"] = "Bahiram"
dic[3] = 6677
print(dic)

