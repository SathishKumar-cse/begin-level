word=input("Enter the sentence: ")
length=len(word)
i=0
count=0
while i<length:
    if word[i]>='0' and word[i]<='9':
        print(word[i])
        count=count+1
    i+=1
print("count of numbers",count)