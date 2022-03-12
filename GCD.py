no1,no2=120,105
div=2
if no1>no2:
    small=no2
if no1<no2:
    small=no1
while div<=small:
    if no1%div==0 and no2%div==0:
        last=div
    div+=1
print("for",no1,no2 ,",greatest common divisior (GCD) is",last)
