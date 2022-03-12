no=int(input("Enter the Number: "))
div=2
while div<no:
    if no%div==0:
        print("Not prime")
        break
    else:
        print("prime")
    div+=1
