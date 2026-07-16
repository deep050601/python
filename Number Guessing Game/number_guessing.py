import random
import time

print("welcome to number guessing game \npress enter to start ")
input()
level = int(
    input("Enter difficulty level \n1.Easy \n2.Medium \n3.Hard \nenter 1/2/3 : ")
)

if level == 1:
    attampt = 8
    print(f"\nyou choose Easy, you have {attampt} attampt ")
elif level == 2:
    attampt = 6
    print(f"\nyou choose Medium, you have {attampt} attampt ")
else:
    attampt = 4
    print(f"\nyou choose Hard, you have {attampt} attampt ")
time.sleep(0.5)
print("computer is guessing a number.....")
time.sleep(1)
print("\ncomputer guessed number between 0 to 25 " )
time.sleep(1)
print("\nnow is your time to guess which number computer have guess ")

computer_num = random.randint(0, 25)

i = 0
while attampt > i:
    i += 1
    time.sleep(1)
    user_num = int(input("\nnow, enter your guessed number : "))
    if user_num == computer_num:
        print("congratulations!! you guessed it right")
        print(f"you completed in {i} attampt")
        break
    elif user_num > computer_num:
        print("guessed high!!")
    elif user_num < computer_num:
        print("guessed low!!")

if attampt == i:
    print("you have o attampt left ")
    print(f"computer guessed {computer_num}")
