from multiprocessing import RLock
import random

while True:

    choices = ['rock','paper','scissors','lizard','spock']

    computer = random.choice(choices)
    player = None


    while player not in choices:
 
        player = input("would you like to play? If so please type in your selection. Rock, Paper, Scissors, Lizard, Spock?: ").lower()

        if player == computer:
            print("The computer seletced " + computer)
            print("You selected " + player)
            print("Tie !")      
        elif player == "rock":
            if computer == "paper":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Paper covers Rock. You Lose !!! ")
            if computer == "scissors":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Rock cruches Scissors. You Win !!!")
            if computer == "lizard":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Rock kills Lizard. You Win !!! ")
            if computer == "spock":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Spock vaporizes Rock. You Lose !!! ")
        elif player == "paper":
            if computer == "rock":
                print("The computer selected" + computer)
                print("You selected " + player)
                print("Paper covers Rock. You Win !!! ")
            if computer == "scissors":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Scissors cut Papaer. You Lose !!! ")
            if computer == "lizard":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Lizard eats Paper. You Lose !!! ")
            if computer == "spock":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Paper disproves Spock. You Win !!! ")
        elif player == "scissors":
            if computer == "rock":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Rock crushes Scissors. You Lose !!! ")
            if computer == "paper":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Scissors cuts Paper. You Win !!! ")
            if computer == "lizard":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Scissors decapitate Lizard. You Win !!!")
            if computer == "spock":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Spock smashes Scissors. You Lose !!! ")
        elif player == "lizard":
            if computer == "rock":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Rock crushes Lizard. You Lose !!! ")
            if computer == "paper":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Lizard eats Paper. You Win !!! ")
            if computer == "scissors":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Scissors decapitate Lizard. You Lose !!! ")
            if computer == "spock":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Lizard poinsions Spock. You Win !!! ")
        elif player == "spock":
            if computer == "rock":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Spock vaporizes Rock You Win !!!")
            if computer == "paper":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Paper disproves Spock. You Lose !!! ")
            if computer == "scissors":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Spock crushes Scissors. You Win !!! ")
            if computer == "lizard":
                print("The computer selected " + computer)
                print("You selected " + player)
                print("Lizard posions Spock. You Lose !!! ")

            

print("It was nice playing with you have a great day and I will see you soon. Good Bye! ")
            


