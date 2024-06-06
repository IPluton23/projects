# 2 Players Tic Tac Toe game
# A-C row selection, 1-3 column selection

# DONE: Printing board in console
# DONE: User input + Printing moves, Needs to check if cell is already taken
# DONE: Commands: 'play' for starting, 'help' for manual, 'tournament' - bo3/bo5
# DONE: Replaying
# DONE Win checking
# Players' names
# Saving moves


# Changing row letter to board's index
dic = {
    "A": 0,
    "B": 1,
    "C": 2
}
# Game's board
arr = [[" " for x in range(3)] for y in range(3)]
# Move counter
count = 0
# P1 move:
p1 = None
# P2 move:
p2 = None


# Printing board in console
def print_board(board):
    for i in range(3):
        print(board[i][0] + "\t|\t" + board[i][1] + "\t|\t" + board[i][2])
        if i < 2:
            print("----+-------+----")


# Function for move validation
def is_valid(move):
    # If out of range
    if len(move) < 2 or len(move) > 2 or move[0] < "A" or move[0] > "C" or move[1] < "1" or move[1] > "3":
        return False
    else:
        # If field is already taken
        if arr[dic.get(move[0])] [int(move[1]) - 1] != " ":
            return False
        else:
            return True


# SPAGHETTI CODE !!!
# symbol is X or O
# Checks if game is won
def is_won(symbol, move):
    match move[0]:
        case'A':
            if arr[0][0] == symbol and arr[0][1] == symbol and arr[0][2] == symbol:
                return True
            else:
                match int(move[1]):
                    case 1:
                        if (arr[1][0] == symbol and arr[2][0] == symbol) or (arr[1][1] == symbol and arr[2][2] == symbol):
                            return True
                        else:
                            return False
                    case 2:
                        if arr[1][1] == symbol and arr[2][1] == symbol:
                            return True
                        else:
                            return False
                    case 3:
                        if (arr[1][2] == symbol and arr[2][2] == symbol) or (arr[1][1] == symbol and arr[2][0] == symbol):
                            return True
                        else:
                            return False
        case 'B':
            if arr[1][0] == symbol and arr[1][1] == symbol and arr[1][2] == symbol:
                return True
            else:
                match int(move[1]):
                    case 1:
                        if arr[0][0] == symbol and arr[2][0] == symbol:
                            return True
                        else:
                            return False
                    case 2:
                        if (arr[0][1] == symbol and arr[2][1] == symbol) or (arr[0][0] == symbol and arr[2][2] == symbol) or (arr[0][2] == symbol and arr[2][0] == symbol):
                            return True
                        else:
                            return False
                    case 3:
                        if arr[0][2] == symbol and arr[2][2] == symbol:
                            return True
                        else:
                            return False
        case 'C':
            if arr[2][0] == symbol and arr[2][1] == symbol and arr[2][2] == symbol:
                return True
            else:
                match int(move[1]):
                    case 1:
                        if (arr[1][0] == symbol and arr[0][0] == symbol) or (arr[1][1] == symbol and arr[0][2] == symbol):
                            return True
                        else:
                            return False
                    case 2:
                        if arr[1][1] == symbol and arr[0][1] == symbol:
                            return True
                        else:
                            return False
                    case 3:
                        if (arr[1][2] == symbol and arr[0][2] == symbol) or (arr[1][1] == symbol and arr[0][0] == symbol):
                            return True
                        else:
                            return False


# Players inputs
def p1_input():
    # PLAYER 1:
    global p1
    print("P1 enter your move:")
    p1 = input().upper()

    # Move validation
    while is_valid(p1) is False:
        print("Invalid move, please enter correct value:")
        p1 = input().upper()
    # Inserting move on board
    arr[dic.get(p1[0])] [int(p1[1]) - 1] = "X"




def p2_input():
    # PLAYER 2:
    global p2
    print("P2 enter your move:")
    p2 = input().upper()

    # Move validation
    while is_valid(p2) is False:
        print("Invalid move, please enter correct value:")
        p2 = input().upper()
    # Inserting move on board
    arr[dic.get(p2[0])] [int(p2[1]) - 1] = "O"


def play_game():
    global count
    global arr
    global p1
    global p2

    # Number of moves is odd, so game needs to start outside the loop
    p1_input()
    print_board(arr)
    while count < 4:
        p2_input()
        print_board(arr)
        # Checks if p2 has won
        if is_won('O', p2):
            print("P2 won")
            arr = [[" " for x in range(3)] for y in range(3)]   # Clearing board in case of replay
            break
        p1_input()
        print_board(arr)
        # Checks if p1 has won
        if is_won('X', p1):
            print("P1 won")
            arr = [[" " for x in range(3)] for y in range(3)]  # Clearing board in case of replay
            break
        count += 1




print("Welcome to Tic Tac Toe Game! \n")


while True:
    print("Enter 'p' for play, 'h' for help, or 'q' for quit")
    value = input()
    match value:
        case 'h':
            print("This is classic Tic Tac Toe game \n "
                  "To win the game you need to put 3 symbols vertically, horizontally or diagonally \n"
                  "You select a cell using letters A-C (row) and numbers 1-3 (column) for example: A2")
        case 'p':
            play_game()
        case 'q':
            break

