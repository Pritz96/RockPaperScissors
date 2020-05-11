import random

def isUserInputValid(userChoice):
    if(userChoice== "rock" or userChoice=="paper" or userChoice=="scissors"):
        return "true"
    else:
        return "false"

userScore=0
computerScore=0
while (userScore != 3 and computerScore != 3):
    print("User score: " + str(userScore))
    print("Computer score: " + str(computerScore))
    userInput = ""
    while (isUserInputValid(userInput)=="false"):
        userInput = input("Type 'rock', 'paper' or 'scissors':")
        
    randomNumber = random.randrange(0, 2)

    options = {
        0 : "rock",
        1 : "paper",
        2 : "scissors"
    }

    computersChoice = options[randomNumber]
    print("The computer randomly chose " + computersChoice)

    if(userInput == computersChoice):
        print("You both chose " + userInput +  ", the game is a draw")
    if (userInput=="paper" and computersChoice=="rock"):
        userScore+=1
        print("Paper covers rock, you win!!")
    if (userInput=="rock" and computersChoice=="paper"):
        computerScore+=1
        print("Paper covers rock, you lose!!")
    if (userInput=="rock" and computersChoice=="scissors"):
        userScore+=1
        print("Rock smashes scissors, you win!!")
    if (userInput=="scissors" and computersChoice=="rock"):
        computerScore+=1
        print("Rock smashes scissors, you lose!!")
    if (userInput=="scissors" and computersChoice=="paper"):
        userScore+=1
        print("Scissors cut paper, you win!!")
    if (userInput=="paper" and computersChoice=="scissors"):
        computerScore+=1
        print("Scissors cut paper, you lose!!")

print("User score: " + str(userScore))
print("Computer score: " + str(computerScore))
if(userScore == 3):
    print("USER WINS 3 GAMES")
if(computerScore==3):
    print("COMPUTER WINS 3 GAMES")

