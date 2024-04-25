import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alph = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():

    user_input = input("Please enter your word: ")
    try:
        nato_code = [nato_alph[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(nato_code)


generate_phonetic()


# user_input = input("Please enter your word: ")
# try:
#     nato_code = [nato_alph[letter.upper()] for letter in user_input]
# except KeyError:
#     is_good = False
#     while not is_good:
#         print("Sorry, only letters in the alphabet please")
#         user_input = input("Please enter your word: ")
#         try:
#             nato_code = [nato_alph[letter.upper()] for letter in user_input]
#             is_good = True
#         except KeyError:
#             is_good = False
# finally:
#     print(nato_code)
