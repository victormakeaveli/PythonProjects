#I made a 'simple' game in order to get the rust off of my fingers
#there's much to do:
#when someone wins
#when theres no turns left.

from random import shuffle

turn = True
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
possibility = [x for x in range(1,10)]

def game():
    """
    This function runs the game itself 
    calling all the other functions
    """

    global turn, possibility

    print("=" * 19, "Welcome to my Tick Tae Toe Game","=" * 19)
    print('\n'*1)
    display()
    in_game = True

    while in_game:
        if len(possibility) == 0:
            print('game over')
            in_game = False
            continue

        if turn:
            positioning()
            turn = False
            continue

        else:
            computer_logic()
            turn = True
 
        display()

def play_choice():
    """
    This function asks the user if he wants to keep playing
    """

    print(' '*18,'do you wanna keep playing? y/n')
    choice = input(' '*34)

    if choice == 'y':
        return True

    elif choice == 'n':
        return False

    else:         # heheh
        play_choice()

def positioning():
    """
    This function takes the user position choice, validate and return it to be assigned on the display func.
    """
    global board 
 
    tap = None
    # print('\n'*3)
    print(" "*15, 'please tap a tile on the numpad')

    while tap != int and tap not in possibility:
        tap = int(input(' '*34))
        if tap not in possibility: 
            print(" "*15, 'position already used')

    if board[tap] == ' ':                         # If the location selected on the board its an empty string (an empty space, a valid location),
        board.pop(tap)                            # pop the given position on the board removing the empty cell
        board.insert(tap, 'X')                    # insert 'X' on the location selected at the board
        possibility.remove(tap)                   # and update the possibility 
        return board, possibility                             

    else:
        print(" "*15, 'insert a number')
        

def display():
    """
    This function prints the board...
    """
    global board

    #...in a naive way
    print(f' '*25, f'='*17)
    print(f' '*25, f'||[{board[7]}]||[{board[8]}]||[{board[9]}]||')
    print(f' '*25, f'||[{board[4]}]||[{board[5]}]||[{board[6]}]||')
    print(f' '*25, f'||[{board[1]}]||[{board[2]}]||[{board[3]}]||')
    print(f' '*25, f'='*17)

    return board

def computer_logic():
    """
    This function randomly selects a position, doing the opponent.
    """
    global board
    global possibility

    done = False
    while done == False:

        shuffle(possibility)
        tile = possibility[0]

        if board[tile] == ' ' and tile in possibility:
            board.pop(tile)
            board.insert(tile, 'O')
            possibility.remove(tile)
            done = True

        else:
            pass
        

    return board, possibility

game()
