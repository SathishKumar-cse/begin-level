def game(guess):

    if mind>guess:
        print("your guess is too small")
    elif mind<guess:
        print("your guess is too large ")
    else:
        print("corrected")

mind=8
while True:

 guess=int(input("Enter the Number between 1 to 10:"))
 game(guess)