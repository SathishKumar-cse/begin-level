def nestedif(n1,n2,n3):
    if n1>n3:
        if n1>n3:
            print(n1,"is big number amoung other numbers")
    elif n2>n1:
         if n2>n3:
             print(n2,"is big number amoung other numbers")
         else:
             print(n3,"is big numper amoung other numbers")
n1=int(input("Enter the first number:  "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number:  "))
nestedif(n1,n2,n3)