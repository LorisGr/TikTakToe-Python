#importing the necessary modules
import random

#creating the tic tac toe board
board = [" " for i in range(9)]

#defining the function to print the game board
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

#defining the function to get user's move
def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
        
    print("Your turn player {}".format(number))
    
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice -1] == " ":
        board[choice -1] = icon
    else:
        print()
        print("That space is taken!")

#defining the ai's move
def ai_move(icon):
    if icon == "X":
        number = 2
    elif icon == "O":
        number = 1
        
    #possible winning combinations
    winning_combinations = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    
    #checking if the board has a winning combination
    for i in winning_combinations:
        if board[i[0]] == board[i[1]] == icon:
            move = i[2]
            if board[move] == " ":
                board[move] = icon
                return
        elif board[i[0]] == board[i[2]] == icon:
            move = i[1]
            if board[move] == " ":
                board[move] = icon
                return
        elif board[i[1]] == board[i[2]] == icon:
            move = i[0]
            if board[move] == " ":
                board[move] = icon
                return
    
    #checking if the opponent has a winning combination
    if icon == "X":
        opp_icon = "O"
    elif icon == "O":
        opp_icon = "X"
        
    for i in winning_combinations:
        if board[i[0]] == board[i[1]] == opp_icon:
            move = i[2]
            if board[move] == " ":
                board[move] = icon
                return
        elif board[i[0]] == board[i[2]] == opp_icon:
            move = i[1]
            if board[move] == " ":
                board[move] = icon
                return
        elif board[i[1]] == board[i[2]] == opp_icon:
            move = i[0]
            if board[move] == " ":
                board[move] = icon
                return
    
    #choosing a random move if no winning combination is present
    while True:
        move = random.randint(0,8)
        if board[move] == " ":
            board[move] = icon
            return

#defining the function to check if the game is a tie
def is_tie():
    if " " not in board:
        return True
    else:
        return False

#defining the function to check if there is a winner
def is_winner(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
            return True
    else:
        return False
    
#defining the main game loop
while True:
    print_board()
    player_move("X")
    print_board()
    if is_winner("X"):
        print("X Wins! Congratulations!")
        break
    elif is_tie():
        print("Its a tie!")
        break
    ai_move("O")
    if is_winner("O"):
        print_board()
        print("O Wins! Congratulations!")
        break
    elif is_tie():
        print("Its a tie!")
        break