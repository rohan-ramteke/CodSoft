print("Choices :")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
print()


Flag = True
while Flag == True:
    choice=int(input("Enter your choice (1-5) -- "))
    print()
    if choice==1:
        num1=input("Enter First number:")
        num2=input("Enter Second number:")
        print("RESULT= " , int(num1)+int(num2))
        print()
    elif choice==2:
        num1=input("Enter First number:")
        num2=input("Enter Second number:")
        print("RESULT= " , int(num1)-int(num2))
        print()
    elif choice==3:
        num1=input("Enter First number:")
        num2=input("Enter Second number:")
        print("RESULT= " , int(num1)*int(num2))
        print()
    elif choice==4:
        num1=input("Enter First number:")
        num2=input("Enter Second number:")
        print("RESULT= " , float(num1)/float(num2))
        print()
    elif choice==5:
        Flag = False
        print("Thank Youu !!")
    else:
        print("Wrong Input !! Try Again ...")
        print()

