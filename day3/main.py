# price = 0
# height = input("Please input your height in cm: ")
# if height > 120:
#     age = int(input("Please enter your age: "))
#     if age < 12:
#         price += 5
#     elif age < 18:
#         price += 7
#     elif age < 45:
#         price += 12
#     else:
#         print("Tickets are free for senior citizens")
#     want_photos = input("Would you like to get photos?(yes/no").lower()
#     if want_photos == "yes":
#         price += 3
#     print(f"Your ticket cost is ${price}")
# else:
#     print("Sorry, you can't ride")


"""Love Calculator"""
#
#
# print("Welcome to Love Calculator")
# name1 = input("What is your name?\n").lower()
# name2 = input("What is their name?\n").lower()
# full_name = name1 + name2
# true = 0
# love = 0
# true += full_name.count('t')
# true += full_name.count('r')
# true += full_name.count('u')
# true += full_name.count('e')
# love += full_name.count('l')
# love += full_name.count('o')
# love += full_name.count('v')
# love += full_name.count('e')
# score = int(str(true) + str(love))
# if score<10 or score>90:
#     print(f"Your score is {score}, you go together like coke and mentos")
# elif 40<=score<=50:
#     print(f"Your score is {score}, you are alright together")
# else:
#     print(f"Your score is {score}")


print("Welcome to Treasure island.\nYour mission is to find the treasure")
direction = input("Left or right?").lower()
if direction == "left":
    condition = input("Swim or wait?").lower()
    if condition == "wait":
        which_door = input("Which door?(Red/Yellow/Blue)").lower()
        if which_door == "yellow":
            print("You win")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
