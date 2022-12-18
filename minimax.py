import random
board ={1:' ',2:' ',3:' ',
        4:' ',5:' ',6:' ',
        7:' ',8:' ',9:' ',}
    
def printBoard(board):
    print(board[1] + ' |' +board[2] + ' |' +board[3] )
    print('--+--+--')
    print(board[4] + ' |' +board[5] + ' |' +board[6] )
    print('--+--+--')
    print(board[7] + ' |' +board[8] + ' |' +board[9] )
    print("................................")


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
    if(position in range(1,10)):
        if posFree(position):
            board[position]=letter
            printBoard(board)
            if(checkForWin()):
                if(letter=='X'):
                    print("Bot Wins!!")
                    exit()
                else:
                    print("Player Wins!")    
                    exit()
            if(checkDraw()):
                print("Draw!")
                exit()
            return
                
                    
        else:
            print("Position is not free choose some other position")    
            position=int(input())
            insert(letter,position)
            return
    else:
        print("Position is invalid..Enter the position again: ")    
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
    bestScore= -800
    bestMove=0
    
    for key in board.keys():
        if(board[key]==' '):
            board[key]=bot
            score= minimax(board,False)
            
            board[key]=' '
            if(score > bestScore):
                bestScore= score
                bestMove=key 
    insert(bot,bestMove)
    return


#OWN    
def minimax(board,isMaximizing):
        if (checkWhichLetterWon(bot)):
            return 1
        elif (checkWhichLetterWon(player)):
            return -1
        elif checkDraw():
            return 0
        
        if (isMaximizing):
            bestScore= -800
            for key in board.keys():
                if(board[key]==' '):
                    board[key]=bot
                    score= minimax(board, False)
                    board[key]=' '
                    if(score > bestScore):
                        bestScore= score          
            return bestScore
        else:
            bestScore= 800
            for key in board.keys():
                if(board[key]==' '):
                    board[key]=player
                    score= minimax(board ,True)
                    board[key]=' '
                    if(score < bestScore):
                        bestScore= score
            return bestScore




def playerFirst():   
    while not checkForWin():
        playerMove()
        botMove()        
def botFirst():
    while not checkForWin():
        botMove()
        playerMove()    


demoBoard ={1:'1',2:'2',3:'3',
        4:'4',5:'5',6:'6',
        7:'7',8:'8',9:'9',}

print("Welcome To The Unbeatable Tic Tac Toe")
print( "This is the configuration for the game...")
printBoard(demoBoard)
print("Do you want to play first?(Type y/n)")
c= input()
if(c=="Y" or c=="y"):     
    playerFirst()
else:
    # botFirst()
    insert(bot,random.randint(1,9))
    playerFirst()
    
    
    

   
    