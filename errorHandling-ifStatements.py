
def checkTrue():

    while True:
        try:
            print("Please enter 3 numbers: ")
            print("\n" *2)
            a = int(input('Number 1: '))
            b = int(input('Number 2: '))
            c = int(input('Number 3: '))

            if a == b or a == c or b == c:
                print("2 or more of the numbers you entered are equal to each other.")
                break
                    
            else:
                print("None of the numbers you entered are equal to one another.")
                break
                    

        except (NameError, ValueError):
            print("You did not input a number, please try again.")



checkTrue()
