# needed to clear the terminal screen
import os
# epic time delays
import time 

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
    # checks first diagonal
    item = board[0][0]
    for row in range(side_len):
        # if it failes, check second diagonal and break
        if board[row][row] != item or board[row][row]  == ' ':
            # check second diagonal
            item = board[0][side_len - 1]
            for row in range(side_len):
                # if it failes, both diagonals are not full
                if board[row][side_len - 1 - row] != item or\
                   board[row][side_len - 1 - row] == ' ':
                    return False
            break
    return True

# check if somebody met one of the three win conditions
def winner(board):
    return any([diagonal_winner(board), row_winner(board),
                column_winner(board)])

# format the board and return
def format_board(board):
    joined_rows = []
    divid_string = ""
    # calculate the top string
    top_string = " |"
    for i in range(len(board[0])):
        top_string += f"{i + 1}|"
    joined_rows.append(top_string)
    # calculates the dividing string
    for i in range(2 * len(board[0]) + 2):
        if i % 2:
            divid_string += '+'
        else:
            divid_string += '-'
    joined_rows.append(divid_string)
    # adds the board to the top 2 lines
    board_size = len(board)
    for i in range(board_size):
        joined_rows.append(f"{i + 1}|{'|'.join(board[i])}|")
        joined_rows.append(divid_string)
    return "\n".join(joined_rows)

# makes a turn
def make_turn(x_or_o, board):
    if x_or_o:
        c = 'X'
    else:
        c = 'O'
    x = input(f'{c} row? ')
    y = input(f'{c} column? ')
    x, y = [int(x) - 1, int(y) - 1]
    if (board[x][y] == ' '):
        board[x][y] = f'{c}'
    else:
        print("Wrong field")
        board = make_turn(x_or_o, board)
    return board

def make_board(size):
    board = []
    for i in range(size):
        board.append([' '] * size)
    return board

# congratulates the winner with a nuclear mushroom
def mushroom_win(winner):
        print(f'''










 _____.,-#%&$@%#&#~,._____
''')
        time.sleep(0.6)
        clear_terminal()
        print(f'''






          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
''')
        time.sleep(0.6)
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

def play_game():
    # get the board size
    size = input("Enter the board size (default - 3): ")
    # checks if size is a number
    if size.isdigit():
        size = int(size)
    else:
        size = 3
    # create an empty board
    board = make_board(size)
    # determines whether it's X's turn or not, False by default
    xturn = False 
    # clear the terminal before the game starts
    clear_terminal()
    # iterates while there's no winner
    turns = 0
    while not winner(board) and not turns == size * size:
        # iterates turns
        turns += 1 
        xturn = not xturn
        # makes a turn
        print(format_board(board))
        board = make_turn(xturn, board)
        clear_terminal()
        # prints the board after a player makes a move
     
    # in case of a draw
    if turns == size * size and not winner(board):
        print(f"""
        ===================
        === It's a draw ===
        ===================
        """)
    else:
        if xturn:
            mushroom_win('X')
        else:
            mushroom_win('O')

play_game()
