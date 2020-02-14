import getpass
import random

play1 = input("Welcome to Rock Paper Scissors\nPlease enter your name Player A: ")
play2 = input("Please enter your name Player B: ")

players = [play1, play2] #Puts both players into a list so that they can be selected randomly

fstplay = random.choice(players)    #Selects the first person to play out of the two names
players.remove(fstplay)             #Removes the name that was selected as the first player. This will make the second player be the 0th index

fstatk = int(getpass.getpass("%s has been randomly selected to start the game\n%sPlease choose your weapon\n1. Rock\n2. Paper\n3. Scissors\nEnter your choice: "%(fstplay,fstplay)))
sndatk = int(getpass.getpass("%s Please choose your weapon\n1. Rock\n2. Paper\n3. Scissors\nEnter your choice: "%(players)))
print("Results: %s (%d) vs %s (%d)"%(fstplay,fstatk,players,sndatk))
if fstatk == sndatk:
    print("It was a draw! No one wins. Good day sir.")
elif fstatk == 1:
    if sndatk == 3:
        print("%s wins!"%(fstplay))
    else:
        print("%s wins!"%(players))
elif fstatk == 2:
    if sndatk == 1:
        print("%s wins!"%(fstplay))
    else:
        print("%s wins!"%(players))
elif fstatk == 3:
    if sndatk == 2:
        print("%s wins!"%(fstplay))
    else:
        print("%s wins!"%(players))