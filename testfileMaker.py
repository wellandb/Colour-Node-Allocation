import random

# Creates a test file automatically 
# Size of test, must be greater than 1
size = 20

file = open('test.txt', 'w')
string = ''
interferring = ['' for x in range(size)] 
for i in range(1,size+1):
    for j in range(random.randint(1,4)):
        value = random.randint(1,size)
        run = 0
        while (value == i or interferring[i-1].find(str(value)) != -1) and run < 3:
            value = random.randint(1,size)
            run += 1
        if not(run < 3):
            continue
        interferring[i-1] = interferring[i-1] + str(value) + ' '
        interferring[value-1] = interferring[value-1] + str(i) + ' '

for i in range(size):
    string = string + str(i+1) + ' ' + interferring[i] + '\n'

file.write(string)
file.close()