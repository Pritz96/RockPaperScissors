import random

validOptions = ["rock", "paper", "scissors"]

def isUserInputValid(userChoice):
    if userChoice in validOptions:
        return True
    else:
        return False

userScore, computerScore = 0, 0
while (userScore != 3 and computerScore != 3):
    print("User score: " + str(userScore))
    print("Computer score: " + str(computerScore))
    userInput = ""
    while (not isUserInputValid(userInput)):
        userInput = input("Type one of the following: '" + "', '".join(validOptions) + "': ")
        
    userChoice = validOptions.index(userInput)

    cpuChoice = random.randrange(0, len(validOptions)-1)
    computersChoice = validOptions[cpuChoice]

    d = (len(validOptions) + userChoice - cpuChoice) % len(validOptions)

    print("The computer chose " + computersChoice)
    
    if d == 1:
        print ("You win!")
        userScore+=1
    elif d == 2:
        print("Computer wins!")
        computerScore+=1
    else:
        print ("A draw!")

print("User score: " + str(userScore))
print("Computer score: " + str(computerScore))
if(userScore == 3):
    print("USER WINS 3 GAMES")
if(computerScore==3):
    print("COMPUTER WINS 3 GAMES")

