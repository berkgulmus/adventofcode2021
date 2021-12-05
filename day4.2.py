

file = open('inputDay4.txt', 'r')
line = file.readline()

# creating a dictionary for the coming up order of the numbers
line = line.strip("\n")
splitLine = line.split(",")
orderObj = {}
for (indx, element) in enumerate(splitLine):
    orderObj[element] = indx+1

boards = []


# this dictionary holds board->(win times of all its rows & columns, first win time)
winTimes = []
counter = 0


# reading the boards and calculating their win conditions
line = file.readline()
while line:
    board = []
    board.append(file.readline().strip("\n"))
    board.append(file.readline().strip("\n"))
    board.append(file.readline().strip("\n"))
    board.append(file.readline().strip("\n"))
    board.append(file.readline().strip("\n"))

    newBoard = []
    boardOrder = []
    for indx, row in enumerate(board):
        boardOrder.append([])
        newRow = []
        newRow.append(row[0:2].strip(" "))
        boardOrder[indx].append(orderObj[row[0:2].strip(" ")])
        newRow.append(row[3:5].strip(" "))
        boardOrder[indx].append(orderObj[row[3:5].strip(" ")])
        newRow.append(row[6:8].strip(" "))
        boardOrder[indx].append(orderObj[row[6:8].strip(" ")])
        newRow.append(row[9:11].strip(" "))
        boardOrder[indx].append(orderObj[row[9:11].strip(" ")])
        newRow.append(row[12:14].strip(" "))
        boardOrder[indx].append(orderObj[row[12:14].strip(" ")])
        newBoard.append(newRow)
    boards.append(newBoard)

    winTime = {}
    # calculating win time required for each row
    for indx, row in enumerate(boardOrder):
        winTime["row" + str(indx)] = max(row)

    # calculating win time required for each column
    for i in range(5):
        column = []
        for j in range(5):
            column.append(boardOrder[j][i])
        winTime["col" + str(i)] = max(column)

    # calculating win time required for first win
    firstWinTime = min(winTime.values())
    winTime["first win"] = firstWinTime

    winTimes.append({("board " + str(counter)): winTime})
    # print(winTime,counter)
    counter += 1
    line = file.readline()

# calculating winning board
tempArr = []
counter = 0
for wintime in winTimes:
    tempArr.append(wintime["board "+str(counter)]["first win"])
    counter += 1

winninBoardsNumber = (tempArr.index(max(tempArr)))
winningTime = (winTimes[winninBoardsNumber]
               ["board "+str(winninBoardsNumber)]["first win"])
totalPoint = 0
for i in range(len(boards[winninBoardsNumber])):
    for j in range(len(boards[winninBoardsNumber][i])):
        if(orderObj[str(boards[winninBoardsNumber][i][j])] > winningTime):
            totalPoint += int(boards[winninBoardsNumber][i][j])


totalPoint*=int(list(orderObj.keys())[winningTime-1])
print(totalPoint)
