greeting = 'Good Morning'
if greeting == 'Morning':
    print('Condition Matches')
else:
    print('Condition do not matches')

print('If else condition completed')

# for Loop
obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

# Sum of first 5 natural numbers
summation = 0
for j in range(1,6):    # range(i,j) -> i to j-1
    summation = summation + j
print(summation)

print('**************')
for k in range(1,8,2):
    print(k)
print('******* Skipping First Index *******')
for m in range(8):
    print(m)
print('******* While Loop *******')
# While Loop
it = 4
while it>1:
    print(it)
    it = it-1