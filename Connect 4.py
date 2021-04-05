def drawField(field):
    for row in range(11):
        practicalRow = int(row/2)
        if row%2 == 0:
            for column in range(13):
                practicalColumn = int(column/2)
                if column%2 == 0:
                    if column !=12:
                        print(field[practicalColumn][practicalRow], end = "")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end = "")
        else:
            print("-------------")
2
Player = 1
currentField = [ [" ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " "],
[" ", " ", " ", " ", " ", " ", " "] ]
drawField(currentField)
gameOver = 0
while(True):
    
    def win():
        for element in currentField:
            global gameOver
            winCondition = 0
            winCondition = element.count("X")
            if winCondition >= 4:
                print("\nPlayer 1 wins!")
                gameOver = 1
            winCondition = element.count("O")
            if winCondition >= 4:
                print("\nPlayer 2 wins!")
                gameOver = 1
        for i in range(7):
            x = 0
            o = 0
            for items in currentField:
                if items[i] == "X":
                    x += 1
                    if x >= 4:
                        print("\nPlayer 1 wins!")
                        gameOver = 1
                        break
                if items[i] == "O":
                    o += 1
                    if o >= 4:
                        print("\nPlayer 2 wins!")
                        gameOver = 1
                        break
        for i in range(7):
            for j in range(4):
                if currentField[i][j] == "X":

                    w = currentField[i][j]
                    a = currentField[i-1][j+1]
                    b = currentField[i-2][j+2]
                    c = currentField[i-3][j+3]
                    if w == a and a == b and b == c:
                        print("Player 1 wins!")
                        gameOver = 1
                        break

                    w = currentField[i][j]
                    x = currentField[i-1][j-1]
                    y = currentField[i-2][j-2]
                    z = currentField[i-3][j-3]
                    if w == x and x == y and y == z:
                        print("Player 1 wins!")
                        gameOver = 1
                        break

                if currentField[i][j] == "O":

                    w = currentField[i][j]
                    a = currentField[i-1][j+1]
                    b = currentField[i-2][j+2]
                    c = currentField[i-3][j+3]
                    if w == a and a == b and b == c:
                        print("Player 1 wins!")
                        gameOver = 1
                        break

                    w = currentField[i][j]
                    x = currentField[i-1][j-1]
                    y = currentField[i-2][j-2]
                    z = currentField[i-3][j-3]
                    if w == x and x == y and y == z:
                        print("Player 1 wins!")
                        gameOver = 1
                        break 
            for j in range(3,7):
                
                if currentField[i][j] == "X":
                    w = currentField[i][j]
                    x = currentField[i-1][j-1]
                    y = currentField[i-2][j-2]
                    z = currentField[i-3][j-3]
                    if w == x and x == y and y == z:
                        print("Player 1 wins!")
                        gameOver = 1
                        break

                if currentField[i][j] == "O":
                    w = currentField[i][j]
                    x = currentField[i-1][j-1]
                    y = currentField[i-2][j-2]
                    z = currentField[i-3][j-3]
                    if w == x and x == y and y == z:
                        print("Player 1 wins!")
                        gameOver = 1
                        break


    if gameOver == 1:
        break
    print("\n")
    print("It is Player " + str(Player) + "\'s turn.\n")
    Move = int(input("Please select the column to drop your piece: ")) 
    Row = -2
    if Player == 1:
        if currentField[Move][Row] == " ":
            currentField[Move][Row] = "X"
            win()
            Player = 2
        else:
            while currentField[Move][Row] != " ":
                Row -= 1
            currentField[Move][Row] = "X"
            win()
            Player = 2
    else:
        if currentField[Move][Row] == " ":
            currentField[Move][Row] = "O"
            win()
            Player = 1
        else:
            while currentField[Move][Row] != " ":
                Row -= 1
            currentField[Move][Row] = "O"
            win()
            Player = 1

    drawField(currentField)