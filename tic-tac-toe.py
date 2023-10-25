# needed to clear the terminal screen
import os
# epic time delays
from time import sleep

# clear the terminal screen
# added this to not bother with the original command
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# checks if a player has already won a row
def row_winner(board):
    side_len = len(board[0])
    for row in range(side_len):
        res = True
        # check if there's a ' ' in the list, if there is go to next iteration
        if ' ' in board[row]:
            continue
        # check if all elements are equal the same (first) value
        item = board[row][0]
        for column in range(side_len):
            if board[row][column] != item:
                res = False
                break
        if res:
            return True
    # if no checks returned True, there were no winning rows
    return False

# checks if a player has already won a column
def column_winner(board):
    side_len = len(board[0])
    for column in range(side_len):
        res = True
        item = board[0][column]
        for row in range(side_len):
            if (
               board[row][column] == ' ' or
               board[row][column] != item 
               ):
                res = False
                break
        if res:
            return res
    return False

# checks if a player has already won a diagonal
def diagonal_winner(board):
    side_len = len(board[0])

    res1 = True
    res2 = True
    # first diagonal
    item = board[0][0]
    for row in range(side_len):
        if board[row][row] != item or board[row][row]  == ' ':
            res1 = False
            break

    # second diagonal
    item = board[0][side_len - 1]
    for row in range(side_len):
        if board[row][side_len - 1 - row] != item or\
           board[row][side_len - 1 - row] == ' ':
            res2 = False
            break

    # if either diagonal is right, the player wins
    return (res1 or res2)

# check if somebody met one of the three win conditions
def winner(board):
    return diagonal_winner(board) or row_winner(board) or\
           column_winner(board)

# print the board to STDOUT
def print_board(board):
    print(f"""
 |1|2|3|
-+-+-+-+
1|{'|'.join(board[0])}|
-+-+-+-+
2|{'|'.join(board[1])}|
-+-+-+-+
3|{'|'.join(board[2])}|
-+-+-+-+
""")
    
# makes a turn
def make_turn(x_or_o, board):
    if x_or_o:
        c = 'X'
    else:
        c = 'O'
    x, y = input(f'{c}? ').split()
    x, y = [int(x) - 1, int(y) - 1]
    if (board[x][y] == ' '):
        board[x][y] = f'{c}'
    else:
        print("Wrong field")
        board = make_turn(x_or_o, board)
    return board

# congratulates the winner with a nuclear mushroom
def mushroom_win(winner):
        print(f'''










 _____.,-#%&$@%#&#~,._____
''')
        sleep(0.6)
        clear_terminal()
        print(f'''






          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
''')
        sleep(0.6)
        clear_terminal()
        print(f'''
     _.-^^---....,,--       
 _--                  --_  
<         /-====-\       >)
|         |{winner} WINS|        | 
 \._      \-====-/     _./  
    ```--. . , ; .--\'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
''')
# "Mushroom cloud" from https://www.asciiart.eu/weapons/explosives

def main():
    # defines an empty board and prints it
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    # determines whether it's X's turn or not, False by default
    xturn = False 
    # iterates while there's no winner
    clear_terminal()
    while not winner(board):
        # iterates turns
        xturn = not xturn
        # makes a turn
        print_board(board)
        board = make_turn(xturn, board)
        clear_terminal()
        # prints the board after a player makes a move

    if xturn:
        mushroom_win('X')
    else:
        mushroom_win('O')

if __name__ == "__main__":
    main()
