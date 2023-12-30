from images import rock, paper, scissors
import random

images = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
user_choice = input("What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors\n>>")
if user_choice.isnumeric() and 0 <= int(user_choice) <= 2:
    user_choice = int(user_choice)
    print(images[user_choice])
    print(f"Computer choose:\n{images[computer_choice]}")
    if user_choice == 0 and computer_choice == 2:
        print("You Win🏆🎉🏆")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win🏆🎉🏆")
    elif user_choice == 3 and computer_choice == 1:
        print("You Win🏆🎉🏆")
    elif user_choice == computer_choice:
        print("Draw⚖️=")
    else:
        print("You lose😢🤦")
else:
    print(False)
