# snake, water, gun game

import random

print("welcome to game!!")

print("for sanke = 1, water=2 , gun = 3 ")
choise = [1, 2, 3]
ycount = 0
ccount = 0
for round in range(0, 3):
    print(f"welcome in round {round+1}")

    playerchoise = int(input("enter your choise "))

    computerchoise = random.choice(choise)
    print(f"computer choise {computerchoise}")

    if playerchoise == computerchoise:
        print("it`s  draw")
    elif playerchoise == 1 and computerchoise == 2:
        print("you win")
        ycount += 1
    elif playerchoise == 1 and computerchoise == 3:
        print("computer win")
        ccount += 1

    elif playerchoise == 2 and computerchoise == 1:
        print("computer win")
        ccount += 1
    elif playerchoise == 2 and computerchoise == 3:
        print("you win")
        ycount += 1

    elif playerchoise == 3 and computerchoise == 1:
        print("you win")
        ycount += 1
    elif playerchoise == 3 and computerchoise == 2:
        print("computer win")
        ccount += 1
    print("\n")

if ycount == ccount:
    print("match is draw between player and computer")
elif ycount > ccount:
    print(f"player win {ycount} round")
else:
    print(f"computer win {ccount} round")
