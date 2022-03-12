value=int(input("Enter the value:"))
getvalue=value
rev=0
while value>0:
   rev=(rev*10)+value%10
   value=value//10
else:
   print("Reversed value is:",rev)
   if getvalue==rev:
      print("palindrome")
   else:
      print("Not palindrom")