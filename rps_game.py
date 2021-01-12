"""
Hey there!!! Hi
It's just a simple game that stone paper scissor
Here you comes to redy our code, Right!!!
Okey I made some hints for you
"""
#first we importimport random
import random

#now we assing empty score
comp_wins = 0
player_wins = 0

#now we gather the in put
def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return user_choice

#now for computer
def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice
print("let's play")
#we use the loop to ask for input next time
while True:
    print("")
    
    user_choice = Choose_Option()
    comp_choice = Computer_Option()

    print("")

    """Normaly we have a theroy like 
	stone vs paper means stone is a winner,
	paper vs scissor means scissor is a Winner &
	scissor vs stone means stone is a winner
	here also just like that we programe it with if-else concept"""

    if user_choice == "r":
        if comp_choice == "r":
            print("Both are same. so game is tie!.")
        
        elif comp_choice == "p":
            print("The computer chose paper. You lose:)")
            comp_wins += 1
            
        elif comp_choice == "s":
            print("The computer chose scissors. You win:)")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("The computer chose rock. You win:)")
            player_wins += 1
        
        elif comp_choice == "p":
            print("Both are same. so game is tie!.")
            
            
        elif comp_choice == "s":
            print("The computer chose scissors. You lose:(")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("The computer chose rock. You lose:(")
            comp_wins += 1
        
        elif comp_choice == "p":
            print("The computer chose paper. You win:)")
            player_wins += 1
            
        elif comp_choice == "s":
            print("Both are same. so game is tie!.")
    #here score time
    print("")
    print("your's score: " + str(player_wins))
    print("Computer's score: " + str(comp_wins))
    print("")
    
    #here we ask for play more
    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
    #program is end
