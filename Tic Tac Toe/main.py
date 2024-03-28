board = [" "]*9


def display_board(board):
    print(" | ".join(board[0:3]))
    print(" | ".join(board[3:6]))
    print(" | ".join(board[6::]))


def player_input():
    user_input = input("Choose a number between 0 and 8: ")
    if user_input.isdigit():
        if 8 >= int(user_input) >= 0:
            return int(user_input)
        else:
            print("The number you entered is out of range! Please choose between 0 and 8")
            player_input()
    else:
        print("You entered wrong type! Please enter a number ranging from 0 to 8")
        player_input()


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, mark):
    for i in range(0, 3):
        if board[i] == board[i+3] == board[i+6] == mark:
            return True
    for i in range(0,7, 3):
        if board[i] == board[i + 1] == board[i + 2] == mark:
            return True
    if board[0] == board[4] == board[8] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False


def space_check(board, position):
    if " " in board[position]:
        return True
    return False


def full_board_check(board):
    if " " not in board:
        return True
    return False


def replay():
    play_again = input("\nWould you like to play again?(Y/N): ")
    if play_again.lower() == "y":
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')
game_on = True
play = True
while play:
    if not full_board_check(board):
        while game_on:
            print("\nPlayer1:")
            display_board(board)
            player_1 = player_input()
            while not space_check(board, player_1):
                print("This position is taken! Please choose another one!")
                player_1 = player_input()
            board = place_marker(board, "X", player_1)
            if win_check(board, "X"):
                print("\nPlayer 1 wins!")
                game_on = False
            else:
                print("\n"*10)
                display_board(board)
                print("Player2:")
                player_2 = player_input()
                while not space_check(board, player_2):
                    print("This position is taken! Please choose another one!")
                    player_2 = player_input()
                board = place_marker(board, "O", player_2)
                if win_check(board, "O"):
                    print("\nPlayer 2 wins!")
                    game_on = False
                print("\n"*10)
    else:
        print("\n\n Draw")

    play = replay()


