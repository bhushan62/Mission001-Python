marks = int(input("Enter Marks: ")) 

if (marks >= 90 ):
    print("Grade A")
elif (marks >= 75 and marks < 90):
    print("Grade B")
elif (marks >=60 and marks <75):
    print("Grade C")
elif (marks >= 35 and marks < 59):
    print("Grade D")
else:
    print("FAIL")

