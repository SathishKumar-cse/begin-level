#add existing last two numbers thats called finobi series
f=-1
s=1
count=1
n=int(input("Enter the maxi num: "))
while True:
    t=f+s
    if t>=n:
        break
    print(t)
    f=s
    s=t
    count+=1
