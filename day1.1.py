
file1 = open('inputDay1.txt', 'r')
Lines = file1.readlines()

count = 0
lastNumb = -1
for line in Lines:
    curNumb = int(line)
    if(lastNumb != -1):
        if(lastNumb < curNumb):
            count += 1
    lastNumb = curNumb
print(count)
