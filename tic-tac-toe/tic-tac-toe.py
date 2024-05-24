# 2 Players Tic Tac Toe game

# DONE: Printing board in console
# User input + Printing moves, Needs to check if cell is already taken
# Counting points
# Players' names
# Commands: play for starting, help for manual

dic = {
    "A": 1,
    "B": 2,
    "C": 3
}
arr = [[" " for x in range(3)] for y in range(3)]


def p1_input():  # A-C row selection, 1-3 column selection
    print("P1 enter your move:")
    p1 = input().upper()
    while p1[0] < "A"  or  p1[0] > "C"  or  p1[1] < "1"  or  p1[1] > "3":
        print("Invalid input, please enter correct value:")
        p1 = input()
    arr[dic.get(p1[0]) - 1][int(p1[1]) - 1] = "X"


def p2_input():
    print("P2 enter your move:")
    p2 = input().upper()
    while p2[0] < "A" or p2[0] > "C" or p2[1] < "1" or p2[1] > "3":
        print("Invalid input, please enter correct value:")
        p2 = input()
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
