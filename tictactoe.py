def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-|-|-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-|-|-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    current_player = players[0]
    game_over = False

    while not game_over:
        print_board(board)
        print(f"It's {current_player}'s turn.")
        move = input("Enter a number between 1 and 9 to make your move: ")
        move = int(move) - 1

        if board[move] == " ":
            board[move] = current_player
            if check_win(board, current_player):
                print(f"{current_player} wins!")
                game_over = True
            elif " " not in board:
                print("Tie game!")
                game_over = True
            else:
                current_player = players[(players.index(current_player) + 1) % 2]
        else:
            print("That spot is already taken. Try again.")

play_game()
