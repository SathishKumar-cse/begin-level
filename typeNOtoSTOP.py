choice=" "
total=0
while not choice=='no':
    mark=int(input("Enter your mark: "))
    total=total+mark
    choice=input("type 'no' to stop")
else:
    print("Total is ",total)
