#if armstrong=153 1*1*1=1,5*5*5=125,3*3*3=27 total=1+125+27=>153,,(armstrong)
value=int(input("Enter the value: "))
getvalue=value
total=0
while value>0:
   dig=value%10
   total=total+(dig*dig*dig)
   value//=10
else:
   if getvalue==total:
      print("Armstrong_number")
   else:
      print("notArmstrong_number")