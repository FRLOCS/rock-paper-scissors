# Play command line Rock-Paper-Scissors
# By: Fanny Lucas
import random 

rps = ["rock", "paper", "scissors"]

print("Lets play rock, paper, scissors! ")


player1 = input("Player1, Choose rock, paper, or scissors ")

player2 = random.choice(rps)


if player1 == "rock":
    print(f"player2 chooses: {player2}")
    if player2 == "rock":
        print("Its a tie!")
    elif player2 == "scissors":
        print("player1 wins!")
    elif player2 == "paper":
        print("player2 wins!")
elif player1 == "scissors":
    print(f"player2 chooses: {player2}")
    if player2 == "scissors":
        print("Its a tie!")
    elif player2 == "rock":
        print("Player2 wins!")
    elif player2 == "paper": 
        print("Player1 wins!")
elif player1 == "paper":
    print(f"player2 chooses: {player2}")
    if player2 == "paper":
        print("Its a tie!")
    elif player2 == "rock":
        print("player2 wins!")
    elif player2 == "scissors":
        print("player2 wins!")
        

    








