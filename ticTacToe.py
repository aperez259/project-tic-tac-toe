choices = ['top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R'] #this list is used to store players' moves and also to check if they are in a winning position


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '} 
def printBoard(board):

    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R']) #this code will print the board



def checkWinner(board, player): 
    print('Checking if '+ player + ' is a winner...')


    if choices[0] == choices[1] == choices[2] == 'X' or choices[3] == choices[4] == choices[5] == 'X' or choices[6] == choices[7] == choices[8] == 'X' or choices[0] == choices[3] == choices[6] == 'X' or choices[1] == choices[4] == choices[7] == 'X' or choices[2] == choices[5] == choices[8]== 'X' or choices[0] == choices[4] == choices[8] == 'X' or choices[2] == choices[4] == choices[6]== 'X': #This code checks the choices list to see if X has a winning position. It checks for the 3 horizontal, 3 vertical and 2 diagonal posibilities.
        print('X wins!') #the above is true, then it prints out that X has won
        return True

    if choices[0] == choices[1] == choices[2] == 'O' or choices[3] == choices[4] == choices[5] == 'O' or choices[6] == choices[7] == choices[8] == 'O' or choices[0] == choices[3] == choices[6] == 'O' or choices[1] == choices[4] == choices[7] == 'O' or choices[2] == choices[5] == choices[8]== 'O' or choices[0] == choices[4] == choices[8] == 'O' or choices[2] == choices[4] == choices[6]== 'O': #This code checks the choices list to see if O has a winning position. It checks for the 3 horizontal, 3 vertical and 2 diagonal posibilities.
        print('Checking if O is a winner...')
        print('O wins!') #the above is true, then it prints out that O has won
        return True
    
    else:
        return False


def startGame(startingPlayer, board):

    

    turn = startingPlayer
    for i in range(9):
        printBoard(board)
        print('Turn for ' + turn + '. Move on which space?')
        player_move = input()
        choices[choices.index(player_move)] = turn #the move that the player enters is then replaced by either an X or an O in the choices list (based on who's turn it is). This list is used as the refence to see who wins.
        board[player_move] = turn


        if ( checkWinner(board, 'X') ):
            break
            quit

        if ( checkWinner(board, 'O') ):
            break
            quit
    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)








    
