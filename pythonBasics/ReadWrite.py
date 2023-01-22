file = open('test.txt.py')
# Read all the contents of file
#print(file.read())

# Read n number of characters by passing parameters
#print(file.read(5))

# Read one single line at a time
#print(file.readline())
#print(file.readline())


# Print line by line using readline method
#line = file.readline()
#while line != '':
 #   print(line)
  #  line = file.readline()

values = ['alphabet', 'blackberry', 'cat', 'doge', 'elephant']
for line in file.readlines():
    print(line)

file.close()
