print("**************CALCULATOR****************")
num1=int(input("Enter the first number\n"))
num2=int(input("Enter the second number\n"))
print("Enter 1 for 'Addition'\n Enter 2 for 'Subtraction'\n Enter 3 for 'Multiplication'\n Enter 4 for 'Division'\n Enter 5 for 'Exponential'\n")
Entered_Number=int(input("Choose the number fron 1 to 5:"))
if Entered_Number==1:
    print("Addition of first and second number:",num1+num2)
elif Entered_Number==2:
    print("Subtraction of first and second number:",num1-num2)
elif Entered_Number==3:
    print("Multiplication of first and second number:",num1*num2)
elif Entered_Number==4:
    print("Division of first and second number:",num1/num2)
elif Entered_Number==5:
    print("Exponential of first and second number:",num1**num2)
else:
    print("Invalid number")