# read the file and store all the lines in list
# reverse the list
# write the list back to the file

with open('test.txt.py', 'r') as reader:
    content = reader.readlines()    # read the text in file
    reversed(content)   # reversed the text in file
    with open ('test.txt.py', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


