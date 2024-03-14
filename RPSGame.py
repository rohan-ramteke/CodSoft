import random

while True:

    print("\n")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissor")
    selection=int(input("Enter your choice:"))
    choices=["Rock", "Paper", "Scissor"]

    if(selection==1):
        player_choice="Rock"
        print("\n")
        print("Player throws",player_choice)
        computer_choice = random.choice(choices)
        print("computer throws",computer_choice)
    elif (selection==2):
        player_choice="Paper"
        print("\n")
        print("Player throws",player_choice)
        computer_choice = random.choice(choices)
        print("computer throws",computer_choice)
    else:
        player_choice="Scissor"
        print("\n")
        print("Player throws",player_choice)
        computer_choice = random.choice(choices)
        print("computer throws",computer_choice)

    if(player_choice == computer_choice):
        print("Tie Game!")
    elif(player_choice == "Rock"):
        if(computer_choice == "Paper"):
            print("Computer Wins!")
        elif(computer_choice == "Scissor"):
            print("Player Wins!")
    elif(player_choice == "Paper"):
        if(computer_choice == "Scissor"):
            print("Computer Wins!")
        elif(computer_choice == "Rock"):
            print("Player Wins!")
    elif(player_choice == "Scissor"):
        if(computer_choice == "Rock"):
            print("Computer Wins!")
        elif(computer_choice == "Paper"):
            print("Player Wins!")

    print("\n")
    print("1.Play Again")
    print("2.Quit")
    selection = int(input("Do you want to play or quit: "))

    if(selection == 2):
        break
