

def createGameBoard(x,y):
    for row in range(x):
        if row%2 == 0:
            for column in range(1,y):
                if column%2 == 1:
                    if column != 5:
                        print(" ",end="")
                    else:
                        print(" ")
                else:
                    print("|",end="")
        else:
            print("-----")
    return True


print(createGameBoard(5,6))