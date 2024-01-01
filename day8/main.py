letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']


def ceaser_cipher(plain_text, cipher_shift, types):
    cipher_text = []
    for letter in plain_text:
        if letter not in letters:
            cipher_text.append(letter)
        else:
            current_shift = letters.index(letter)
            if types == "decode":
                cipher_index = (current_shift + cipher_shift)
                if cipher_index > 25:
                    cipher_index = cipher_index % 26
            else:
                cipher_index = current_shift - cipher_shift
                if cipher_index < -26:
                    cipher_index = cipher_index % -26
            cipher_text.append(letters[cipher_index])

    print(f"\nYour {types}ed text: {''.join(cipher_text)}")


def play_cipher():
    correct_attr = False
    while not correct_attr:
        cipher_type = input("Would you like to 'encode' or 'decode'?\n>>").lower()
        if cipher_type == 'encode' or cipher_type == 'decode':
            correct_attr = True
        else:
            print("Type only 'encode' or 'decode'")
    plain_text = input("Please enter the plain text:\n>>").lower()
    cipher_shift = int(input("Please enter the shift amount:\n>>"))
    ceaser_cipher(plain_text, cipher_shift, cipher_type)


play_again = True
while play_again:
    play_cipher()
    play = input("\nWould you like to use the program one more time?(yes/no)\n>>").lower()
    if play == 'yes':
        play_again = True
        print("\n"*20)
    else:
        play_again = False
        print("Bye")
