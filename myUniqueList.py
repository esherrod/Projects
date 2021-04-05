myUniqueList = []
myLeftovers = []

def appendList(x):
    if x in myUniqueList:
        myLeftovers.append(x)
        return False
    else:
        myUniqueList.append(x)
        return True


print(appendList(1))
print(appendList(2))
print(appendList(2))
print(appendList(3))
print(appendList(4))
print(appendList('Hello'))
print(appendList('Goodbye'))
print(appendList('Test'))
print(appendList('Test'))
print(appendList('Test again'))
print(appendList(1))
print(appendList(1))
print(appendList(1))
print(appendList('Hello'))
print(appendList('Test Over'))

print(myUniqueList)
print(myLeftovers)