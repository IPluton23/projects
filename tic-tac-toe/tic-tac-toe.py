# 2 Players Tic Tac Toe game

# Printing board in console
# User input + Printing moves
# Counting points

dic = {
    "A": 1,
    "B": 2,
    "C": 3
}
arr = [[" "] * 3] * 3


def print_board(board):
    for i in range(3):
        print(board[i][0] + "\t|\t" + board[i][1] + "\t|\t" + board[i][2])
        if i < 2:
            print("----+-------+----")


print_board(arr)
