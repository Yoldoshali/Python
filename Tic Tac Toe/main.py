"""Basic Tic Toe Game. Code has been rated at 9.55/10"""

board = [" "] * 9


def display_board(board_updated):
    """
    Display the updated board
    """
    print(" | ".join(board_updated[0:3]))
    print(" | ".join(board_updated[3:6]))
    print(" | ".join(board_updated[6::]))


def player_input():
    """
    Display user choice as an integer
    """
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


def place_marker(updated_board, marker, position):
    """
    Update the board after user input the position
    """
    updated_board[position] = marker
    return updated_board


def win_check(updated_board, mark):
    """
    Check if the player has won and return True otherwise return False
    """
    for i in range(0, 3):
        if updated_board[i] == updated_board[i + 3] == updated_board[i + 6] == mark:
            return True
    for i in range(0, 7, 3):
        if updated_board[i] == updated_board[i + 1] == updated_board[i + 2] == mark:
            return True
    if updated_board[0] == updated_board[4] == updated_board[8] == mark:
        return True

    return updated_board[3] == updated_board[5] == updated_board[7] == mark


def space_check(current_board, position):
    """
    Check if the position is taken. Return True if it is available otherwise return False
    """
    return " " in current_board[position]


def full_board_check(current_board):
    """
    Check if the board is full. Return True if it is full otherwise return False
    """
    return " " not in current_board


def replay():
    """
    Check if the user wants to play again. Return True if the user wants to play again otherwise return False
    """
    play_again = input("\nWould you like to play again?(y/n): ").lower()
    if play_again == "y":
        return True
    return False


print('Welcome to Tic Tac Toe!')
GAME_ON = True
PLAY = True
while PLAY:
    if not full_board_check(board):
        while GAME_ON:
            print("\nPlayer1:")
            display_board(board)
            player_1 = player_input()
            while not space_check(board, player_1):
                print("This position is taken! Please choose another one!")
                player_1 = player_input()
            board = place_marker(board, "X", player_1)
            GAME_ON = full_board_check(board)
            if win_check(board, "X"):
                print("\nPlayer 1 wins!")
                GAME_ON = False
            else:
                print("\n" * 10)
                display_board(board)
                print("Player2:")
                player_2 = player_input()
                while not space_check(board, player_2):
                    print("This position is taken! Please choose another one!")
                    player_2 = player_input()
                board = place_marker(board, "O", player_2)
                if win_check(board, "O"):
                    print("\nPlayer 2 wins!")
                    GAME_ON = False
                print("\n" * 10)
    else:
        print("\n\n Draw")

    PLAY = replay()
