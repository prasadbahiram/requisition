
ItemsInCart = 0
# If 2 Items will be added in Cart

if ItemsInCart != 2:
   # raise Exception('Products Cart count not matching')
    pass
assert (ItemsInCart == 0)

try:
    with open ('testng.txt.py', 'r') as reader:
        reader.read()

except:
    print('Somehow I reached in this block because there is failure in try block')

try:
    with open ('testng.txt.py', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print('Cleaning up resources')

