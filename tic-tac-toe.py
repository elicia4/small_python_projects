# # row winner for 3 sized side ttt
# def row_winner(board):
#     return (
#            board[0][0] == board [0][1] == board[0][2] and board[0][0] != ' ' or
#            board[1][0] == board [1][1] == board[1][2] and board[1][0] != ' ' or
#            board[2][0] == board [2][1] == board[2][2] and board[2][0] != ' '
#            )

# # column winner for 3 sized side ttt
# def column_winner(board):
#     return (
#            board[0][0] == board[1][0] == board[2][0] and board[0][0] != ' ' or
#            board[0][1] == board[1][1] == board[2][1] and board[0][1] != ' ' or 
#            board[0][2] == board[1][2] == board[2][2] and board[0][2] != ' '
#            )

# # diagonal winner for 3 sized side ttt
# def diagonal_winner(board):
#     return (
#            board[0][0] == board[1][1] == board[2][2] and board[1][1] != ' ' or
#            board[0][2] == board[1][1] == board[2][0] and board[1][1] != ' '
#            )
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

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

# check if somebody won or not
def winner(board):
    return diagonal_winner(board) or row_winner(board) or\
           column_winner(board)

def print_board(board):
    print(f"\n |1|2|3|")
    print(f"-+-+-+-+")
    print(f"1|{'|'.join(board[0])}|")
    print(f"-+-+-+-+")
    print(f"2|{'|'.join(board[1])}|")
    print(f"-+-+-+-+")
    print(f"3|{'|'.join(board[2])}|")
    print(f"-+-+-+-+\n")
    
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

def mushroom_win(winner): # congratulates the winner with a nuclear mushroom
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
