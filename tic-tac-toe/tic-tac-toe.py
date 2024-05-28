# 2 Players Tic Tac Toe game
# A-C row selection, 1-3 column selection

# DONE: Printing board in console
# DONE: User input + Printing moves, Needs to check if cell is already taken
# Players' names
# Commands: 'play' for starting, 'help' for manual, 'tournament' - bo3/bo5
# Replaying
# Win checking
# Saving moves


# Changing row letter to board's index
dic = {
    "A": 1,
    "B": 2,
    "C": 3
}
# Game's board
arr = [[" " for x in range(3)] for y in range(3)]
# Move counter
count = 0


# Printing board in console
def print_board(board):
    for i in range(3):
        print(board[i][0] + "\t|\t" + board[i][1] + "\t|\t" + board[i][2])
        if i < 2:
            print("----+-------+----")


# Function for move validation
def is_valid(move):
    # If out of range
    if move[0] < "A" or move[0] > "C" or move[1] < "1" or move[1] > "3":
        return False
    else:
        # If field is already taken
        if arr[dic.get(move[0]) - 1][int(move[1]) - 1] != " ":
            return False
        else:
            return True


# Players inputs
def p1_input():
    # PLAYER 1:
    print("P1 enter your move:")
    p1 = input().upper()

    # Move validation
    while is_valid(p1) is False:
        print("Invalid move, please enter correct value:")
        p1 = input().upper()
    # Inserting move on board
    arr[dic.get(p1[0]) - 1][int(p1[1]) - 1] = "X"


def p2_input():
    # PLAYER 2:
    print("P2 enter your move:")
    p2 = input().upper()

    # Move validation
    while is_valid(p2) is False:
        print("Invalid move, please enter correct value:")
        p2 = input().upper()
    # Inserting move on board
    arr[dic.get(p2[0]) - 1][int(p2[1]) - 1] = "O"


def play_game():
    global count
    while count < 4:
        p1_input()
        print_board(arr)
        p2_input()
        print_board(arr)
        count += 1

    p1_input()
    print_board(arr)


print("Welcome to Tic Tac Toe Game! \n")
print("Enter 'p' for play, 'h' for help")
value = input()
match value:
    case 'h':
        print("This is classic Tic Tac Toe game \n "
              "To win the game you need to put 3 symbols vertically, horizontally or diagonally \n"
              "You select a cell using letters A-C (row) and numbers 1-3 (column) for example: A2")

play_game()

