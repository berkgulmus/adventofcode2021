depth = 0
horizontal = 0

file = open('inputDay2.txt', 'r')
line = file.readline()
while line:
    splitline = (line.strip("\n")).split(" ")
    code = splitline[0]
    amount = int(splitline[1])
    if(code == "down"):
        depth += amount
    elif(code == "forward"):
        horizontal += amount
    elif("up"):
        depth -= amount
    line = file.readline()
file.close()

print(depth, horizontal)
print(depth*horizontal)
