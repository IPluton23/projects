# 2 Players Tic Tac Toe game
# A-C row selection, 1-3 column selection

# DONE: Printing board in console
# DONE: User input + Printing moves, Needs to check if cell is already taken
# Counting points
# Players' names
# Commands: 'play' for starting, 'help' for manual


# Changing row selection letter to board's index
dic = {
    "A": 1,
    "B": 2,
    "C": 3
}

# Game's board
arr = [[" " for x in range(3)] for y in range(3)]


# Function for move validation
def is_valid(move):
    if move[0] < "A" or move[0] > "C" or move[1] < "1" or move[1] > "3":
        return False
    else:
        if arr[dic.get(move[0]) - 1][int(move[1]) - 1] != " ":
            return False
        else:
            return True


def p1_input():
    print("P1 enter your move:")
    p1 = input().upper()

    # Move validation
    while is_valid(p1) is False:
        print("Invalid move, please enter correct value:")
        p1 = input().upper()

    arr[dic.get(p1[0]) - 1][int(p1[1]) - 1] = "X"


def p2_input():
    print("P2 enter your move:")
    p2 = input().upper()

    # Move validation
    while is_valid(p2) is False:
        print("Invalid move, please enter correct value:")
        p2 = input().upper()

    arr[dic.get(p2[0]) - 1][int(p2[1]) - 1] = "O"



def print_board(board):
    for i in range(3):
        print(board[i][0] + "\t|\t" + board[i][1] + "\t|\t" + board[i][2])
        if i < 2:
            print("----+-------+----")


print("Welcome to Tic Tac Toe Game! \n")
p1_input()
print_board(arr)
p2_input()
print_board(arr)
