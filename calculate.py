print ("~~~~~~~~~ WELCOME!  What would you like to calculate today? ~~~~~~~~~")

userchoice = input("Please enter: ADD (for addition) ||  MIN (for subtraction) || MUL (for multiplication) || DIV (for division): ") 

if userchoice == ( "ADD"):

    num1 = int(input("Enter the first number: "))
    num2 = int (input("Enter the second number: "))

    total = (num1 + num2)
    print ("The sum of two numbers is:",  total )

elif userchoice == ("MIN"):
    num1 = int(input("Enter the first number: "))
    num2 = int (input("Enter the second number: "))

    total = (num1 - num2)
    print ("The division of two numbers is:",  total )

elif userchoice == ("MUL"): 
    num1 = int(input("Enter the first number: "))
    num2 = int (input("Enter the second number: "))

    total = (num1 * num2)
    print ("The multiplication  of two numbers is:",  total )

elif userchoice == ("DIV"): 
    num1 = int(input("Enter the first number: "))
    num2 = int (input("Enter the second number: "))

    total = (num1 / num2)
    print ("The division  of two numbers is:",  total )

else: 
    print ("Wrong Entery! .. Please try again.") 





