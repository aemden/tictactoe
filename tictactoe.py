def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def get_move(player):
    print(f"Player {player}'s turn.")
    while True:
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if row > 2 or col > 2:
            print("Error: Invalid move. Row and column indices must be between 0 and 2.")
        else:
            return row, col

def play_game():
    # initialize board
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # print initial board
    print_board(board)

    # game loop
    for i in range(9):
        player = "X" if i % 2 == 0 else "O"
        row, col = get_move(player)

        # check if move is valid
        while board[row][col] != " ":
            print("That spot is already taken. Try again.")
            row, col = get_move(player)

        # update board
        board[row][col] = player

        # print updated board
        print_board(board)

        # check if player has won
        if (board[0][0] == player and board[0][1] == player and board[0][2] == player) or \
           (board[1][0] == player and board[1][1] == player and board[1][2] == player) or \
           (board[2][0] == player and board[2][1] == player and board[2][2] == player) or \
           (board[0][0] == player and board[1][0] == player and board[2][0] == player) or \
           (board[0][1] == player and board[1][1] == player and board[2][1] == player) or \
           (board[0][2] == player and board[1][2] == player and board[2][2] == player) or \
           (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
           (board[0][2] == player and board[1][1] == player and board[2][0] == player):
            print(f"Player {player} wins!")
            return

    # game is a tie
    print("Tie game.")

# start game
play_game()
