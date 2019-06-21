import random

def int_input(input):
    user_input = raw_input(input)
    return int(user_input)

roundsToPlay = int_input("enter rounds to play: ")

def findPlayerMove(stuff):
    if stuff == "r":
        playerMove = "Rock"
    elif stuff == "p":
        playerMove = "Paper"
    elif stuff == "s":
        playerMove = "Scissors"
    return playerMove

def findSystemMove(stuff):
    if stuff == 1:
        systemMove = "Rock"
    elif stuff == 2:
        systemMove = "Paper"
    elif stuff == 3:
        systemMove = "Scissors"
    return systemMove

playerScore = 0
systemScore = 0

while roundsToPlay > 0 :
    print (str(roundsToPlay) + " rounds left")
    print ("r for rock, p for paper, s for scissors")
    playerChoice = raw_input("Rock Paper or Scissors?  ")
    playerMove = findPlayerMove(playerChoice)
    systemChoice = random.randint(1,3)
    systemMove = findSystemMove(systemChoice)

    if playerMove == "Scissors" and systemMove == "Scissors":
        print("~~draw! nobody scores a point.~~")
    elif playerMove == "Scissors" and systemMove == "Rock":
        print("~~The System scores a point!~~")
        systemScore = systemScore + 1
    elif playerMove == "Scissors" and systemMove == "Paper":
        print("~~The Player scores a point!~~")
        playerScore = playerScore + 1
    elif playerMove == "Paper" and systemMove == "Paper":
        print("~~draw! nobody scores a point.~~")
    elif playerMove == "Paper" and systemMove == "Scissors":
        print("~~The System scores a point!~~")
        systemScore = systemScore + 1
    elif playerMove == "Paper" and systemMove == "Rock":
        print("~~The Player scores a point!~~")
        playerScore = playerScore + 1
    elif playerMove == "Rock" and systemMove == "Rock":
        print("~~draw! nobody scores a point.~~")
    elif playerMove == "Rock" and systemMove == "Scissors":
        print("~~The Player scores a point!~~")
        playerScore = playerScore + 1
    elif playerMove == "Rock" and systemMove == "Paper":
        print("~~The System scores a point!~~")
        systemScore = systemScore + 1
    else: print("error")
    print ("Player: " + str(playerScore) + "  " + "System: " + str(systemScore))
    roundsToPlay = roundsToPlay -1

if roundsToPlay == 0:
    print("FINAL SCORE: " + "Player: " + str(playerScore) + "  " + "System: " + str(systemScore))
    if playerScore > systemScore:
        print("THE PLAYER WINS!!!!!!!!!!!!!!!!!")
    elif playerScore == systemScore:
        print("~~DRAW, NOBODY WINS!!!!!~~")
    else:
        print("~~THE SYSTEM WINS!!!!!!!!!!!!!!!!!~~")
