binary=int(input("Enter the binary value; "))
decimal,i,rem=0,0,0
while binary!=0:
      rem=binary%10
      decimal=decimal+rem*pow(2,i)
      binary=binary//10
      i+=1
else:
   print("decimal value is",decimal)