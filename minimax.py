board ={1:' ',2:' ',3:' ',
        4:' ',5:' ',6:' ',
        7:' ',8:' ',9:' ',}
    
def printBoard(board):
    print(board[1] + ' |' +board[2] + ' |' +board[3] )
    print('--+--+--')
    print(board[4] + ' |' +board[5] + ' |' +board[6] )
    print('--+--+--')
    print(board[7] + ' |' +board[8] + ' |' +board[9] )
    


def checkDraw():
    for key in board.keys():
        if board[key]==' ':
            return False
    return True
    
    
def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False
    
def checkWhichLetterWon(letter):
    if board[1] == board[2] and board[1] == board[3] and board[1] == letter:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == letter):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == letter):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == letter):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == letter):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == letter):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == letter):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == letter):
        return True
    else:
        return False

def posFree(position):
    if(board[position]==' '):
        return True
    else:
        return False
    
def insert(letter,position):
    if posFree(position):
        board[position]=letter
        printBoard(board)
        print("Inserted")
        if(checkDraw()):
            print("Draw!")
            exit()
        if(checkForWin()):
            if(letter=='X'):
                print("Bot Wins!!")
                exit()
            else:
                print("Player Wins!")    
                exit()
        return
            
                
    else:
        print("Position is not free choose some other position")    
        position=int(input())
        insert(letter,position)
        return

player='O'
bot='X'

def playerMove():
    position=int(input("Enter position for O: "))
    insert(player,position)
    return

def botMove():
    bestScore= -1000
    bestMove=0
    
    for key in board.keys():
        if(board[key]==' '):
            board[key]=bot
            score= minimax(board,0,False)
            
            board[key]=' '
            if(score> bestScore):
                bestScore= score
                bestMove=key 
    insert(bot,bestMove)
    return
    
def minimax(board,depth,isMaximising):
    if checkWhichLetterWon(bot):
        return 100
    elif checkWhichLetterWon(player):
        return -100
    elif checkDraw():
        return 0
    
    if isMaximising:
       
        bestScore= -1000
        for key in board.keys():
            if(board[key]==' '):
                board[key]=bot
                score= minimax(board, depth + 1, False)
                board[key]=' '
                if(score> bestScore):
                    bestScore= score          
        return bestScore
    else:
        
        bestScore= 1000
        for key in board.keys():
            if(board[key]==' '):
                board[key]=bot
                score= minimax(board, depth + 1 ,True)
                board[key]=' '
                if(score< bestScore):
                    bestScore= score
        return bestScore
        
while not checkForWin():
    botMove()
    playerMove()
    # if not checkForWin():
   
    