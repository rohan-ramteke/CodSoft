from random import *

choice= ["Rock" , "Paper" , "Scissors"]
pt=int(input("For how many points you want to play : "))
print()
UserPts=0
CPts=0

print("1.Rock \n2.Paper \n3.Scissors\n")
 
for i in range(pt):
    opt=input("Enter your Choice : ")
    comp=choice[randint(0,2)]
    if opt==comp:
        print("Tie !")
        print()
    elif opt=="1":
        if comp=="Paper":
            CPts+=1
            print("Computer gets a point !")
        elif comp=="Scissor":
            UserPts+=1
            print("You get a point")
        print()
    elif opt=="2":
        if comp=="Rock":
            UserPts+=1
            print("You get a point !")
        elif comp=="Scissor":
            CPts+=1
            print("Computer gets a point")
        print()
    elif opt=="3":
        if comp=="Rock":
            CPts+=1
            print("Computer gets a point !")
        elif comp=="Paper":
            UserPts+=1
            print("You get a point")
        print()
    else:
        print("Enter a correct choice !!")


print("YOUR SCORE :" , UserPts ,"\t\t", "COMPUTER'S SCORE:" , CPts)
print()

if UserPts==CPts:
    print("Its a Tie ")
elif UserPts>CPts:
    print("Congo ! You are a winner !!")
else:
    print("Computer Wins... !")


    
            
