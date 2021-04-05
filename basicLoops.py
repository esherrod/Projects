
i = 1

while i <= 100:
    # this will print out 'fizz' if a number is divisible by 3, 'buzz' if it is divisible by 5, and 'fizzbuzz' if it is divisible by both
    if not(i%3) and not(i%5):
        print("fizzbuzz")
    elif not(i%3):
        print("fizz")
    elif not(i%5):
        print("buzz")
    else:
        print(i)
    # this will print out the word 'prime' after a number if it is only divisible by 1, and itself
    for x in range(2,i):
        if i%x == 0:
            
            break
    else:
        print("prime")   

    i += 1
