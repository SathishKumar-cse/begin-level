def getmarks(mark):
    if mark>100:
        print("INVAID Marks")
    elif mark>90:
        print("Grade-'A'")
    elif mark>75:
        print("Grade-'B'")
    elif mark>60:
        print("grade-'C'")
    elif mark>50:
        print("Grade-'D'")
    else:
        print("Fail")

marks=int(input("Enter your Total_marks: "))
getmarks(marks)

