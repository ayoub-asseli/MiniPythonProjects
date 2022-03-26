import os

user = int(input("Enter the number to guess: "))
for i in range(100):
    print('\n')

#player
player = int(input("What do you think the number is ? "))

#Set the maximum number of trial
max_trial = 10

#Game process
while max_trial != 1:
    if player < user:
        print("\nWrong, it's higher !")
        max_trial -= 1
        print("You have " + str(max_trial) + " trials left...")
        player = int(input("What do you think the number is ? "))
    elif player > user:
        print("\nWrong, it's lower !")
        max_trial -= 1
        print("You have " + str(max_trial) + " trials left...")
        player = int(input("What do you think the number is ?"))
    elif player == user:
        print("\nCongrats !!!")
        print("You found the right number:", user)
        break

if max_trial == 1:
    print("\nSorry ! You have exhausted your number of trials")
    print("The right number was:", user)
