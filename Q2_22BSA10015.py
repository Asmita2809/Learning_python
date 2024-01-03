#taking input for the marks
marks= int(input("Enter the percentage recieved: "))
if(marks>100 or marks<0):
    print("Please enter valid percentage")
elif (marks>=90):
    print('the garde is S')
elif (marks>=80):
    print('garda=A')
elif(marks>=70): 
    print('grade is B')
elif(marks>=60):
    print("grade is C")
elif(marks>=40):
    print("grade is D")
else:
    print("grade is F")
