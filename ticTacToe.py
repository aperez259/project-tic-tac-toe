def printBoard(board):

    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R']) #this code will print the board



def checkWinner(board, player): 
    print('Checking if '+ player + ' is a winner...')


    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or #This code checks to see if either player has a winning position. It checks for the 3 horizontal, 3 vertical and 2 diagonal posibilities.
    (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or
    (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or
    (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or 
    (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or 
    (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or 
    (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or 
    (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player)) 


def startGame(startingPlayer, board):

    
    turn = startingPlayer
    for i in range(9): #Repeats the loop for a max of 9 times
        printBoard(board)
        print('Turn for ' + turn + '. Move on which space?') #prints asking the player where they want to move
        move = input() #player enters their move
        board[move] = turn #puts the player's move into the board
        if( checkWinner(board, 'X') ): #pulls up checkWinner to see if 'X' is in a winning position
            print('X wins!') #prints that X has won
            break #if X wins, it ends the loop
        elif ( checkWinner(board, 'O') ): #Checks to see if 'O' is in a winning position
            print('O wins!') #prints that O has won
            break #if X wins, it ends the loop
    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)






    
