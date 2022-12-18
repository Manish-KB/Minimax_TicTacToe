board ={1:' ',2:' ',3:' ',
        4:' ',5:' ',6:' ',
        7:' ',8:' ',9:' ',}
    
def printBoard(board):
    print(board[1] + ' |' +board[2] + ' |' +board[3] )
    print('--+--+--')
    print(board[4] + ' |' +board[5] + ' |' +board[6] )
    print('--+--+--')
    print(board[7] + ' |' +board[8] + ' |' +board[9] )
    
printBoard(board)    

def checkDraw():
    for key in board.keys():
        if board[key]==' ':
            return False
    return True
    
    
def checkForWin():
    if(board[1]==board[2] and board[2]==board[3] and board[1] !=' '):
        return True     
    if(board[4]==board[5] and board[5]==board[6] and board[4] !=' '):
        return True 
    if(board[7]==board[8] and board[8]==board[9] and board[7] !=' '):
        return True  
    
    if(board[1]==board[5] and board[5]==board[9] and board[1] !=' '):
        return True  
    if(board[3]==board[5] and board[5]==board[7] and board[3] !=' '):
        return True 
    
    if(board[1]==board[4] and board[4]==board[7] and board[1] !=' '):
        return True 
    if(board[2]==board[5] and board[5]==board[8] and board[2] !=' '):
        return True 
    if(board[3]==board[6] and board[6]==board[9] and board[3] !=' '):
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
            if(letter=='X'or letter=='x'):
                print("Bot Wins!!")
                exit()
            else:
                print("Player Wins!")    
      
       
            
                
    else:
        print("Position is not free choose some other position")    
        position=int(input())
        insert(letter,position)

player='O'
bot='X'

def playerMove():
    position=int(input("Enter position for O: "))
    insert(player,position)
    return

def botMove():
    position=int(input("Enter position for X: "))
    insert(bot,position)
    return


while not checkForWin():
    playerMove()
    if not checkForWin():
        botMove()
    