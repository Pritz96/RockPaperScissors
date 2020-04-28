import random

def isUserInputValid(userChoice):
    if(userChoice== "rock" or userChoice=="paper" or userChoice=="scissors"):
        return "true"
    else:
        return "false"

userInput = ""
while isUserInputValid(userInput)=="false":
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
    print("Paper covers rock, you win!!")
if (userInput=="rock" and computersChoice=="paper"):
    print("Paper covers rock, you lose!!")
if (userInput=="rock" and computersChoice=="scissors"):
    print("Rock smashes scissors, you win!!")
if (userInput=="scissors" and computersChoice=="rock"):
    print("Rock smashes scissors, you lose!!")
if (userInput=="scissors" and computersChoice=="paper"):
    print("Scissors cut paper, you win!!")
if (userInput=="paper" and computersChoice=="scissors"):
    print("Scissors cut paper, you lose!!")
