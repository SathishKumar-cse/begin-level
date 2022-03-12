name=input("what is your name??")
length=len(name)
i=0
count=0
while i<length:
    if name[i] in ['a','e','o','i','u']:
        print(name[i])
        count=count+1
    i+=1
print("count of vowels: ",count)
