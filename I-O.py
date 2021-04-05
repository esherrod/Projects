
fileName = input("Please name the file you will use for Notes: ")
fileName = fileName + ".txt"

#print(fileName)
x = ""

try: 
    with open(fileName, "x") as f:
        f.write(input())
except:
    x = input("That file name already exists. Would you like to:\nRead the File -> \'r\'\nStart the file over -> \'w\'\nAdd to the file -> \'a\'\n")

if x == 'r':
    f = open(fileName,'r')
    file_contents = f.read()
    print(file_contents)
    f.close()
elif x == 'w':
    f = open(fileName, 'w')
    f.write(input())
    f.close()
elif x == 'a':
    f = open(fileName, 'a')
    f.write(input())
    f.close()
