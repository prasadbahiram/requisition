# Self keyword is mandatory for calling variable name sinto method
# instance and class variables have whole different purpose
# constructor name should be __init__


class Calculator:
    num=100   #class variables

 #default constructor
    def __init__(self,a,b):
        self.FirstNumber = a           #Instance Variables
        self.SecondNumber = b         #Instance Variables
        print('I am called automatically when object is created')

    def getdata(self):
        print('I am now executing as Method in class')

    def summation(self):
        return self.FirstNumber + self.SecondNumber + Calculator.num

obj = Calculator(2,3)       #Syntax to create object in python
obj.getdata()
print(obj.summation())

obj1 = Calculator(4,5)       #Syntax to create object in python
obj1.getdata()
print(obj1.summation())