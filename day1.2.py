
file1 = open('inputDay1.txt', 'r')
Lines = file1.readlines()
tempArr = [0, 0, 0]
sumsArray = []
counter = 0
for line in Lines:
    curNumb = int(line)
    tempArr[counter % 3] = curNumb
    counter += 1
    if(counter >= 3):
        sumsArray.append(sum(tempArr))

counter = 0
lastItem = 0
answer = 0
for i in sumsArray:
    if(counter >= 1):
        if(i > lastItem):
            answer += 1

    lastItem = i
    counter += 1
print(answer)
