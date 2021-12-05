depth = 0
horizontal = 0
aim = 0

file = open('inputDay2.txt', 'r')
line = file.readline()
while line:
    splitline = (line.strip("\n")).split(" ")
    code = splitline[0]
    amount = int(splitline[1])
    if(code == "down"):
        aim += amount
    elif(code == "forward"):
        depth += amount * aim
        horizontal += amount
    elif("up"):
        aim -= amount
    line = file.readline()
file.close()

print(depth, horizontal)
print(depth*horizontal)
