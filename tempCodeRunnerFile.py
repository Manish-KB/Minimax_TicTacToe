#net
# def minimax(board, isMaximizing):
#     if (checkWhichLetterWon(bot)):
#         return 1
#     elif (checkWhichLetterWon(player)):
#         return -1
#     elif (checkDraw()):
#         return 0

#     if (isMaximizing):
#         bestScore = -800
#         for key in board.keys():
#             if (board[key] == ' '):
#                 board[key] = bot
#                 score = minimax(board,  False)
#                 board[key] = ' '
#                 if (score > bestScore):
#                     bestScore = score
#         return bestScore

#     else:
#         bestScore = 800
#         for key in board.keys():
#             if (board[key] == ' '):
#                 board[key] = player
#                 score = minimax(board , True)
#                 board[key] = ' '
#                 if (score < bestScore):
#                     bestScore = score
#         return bestScore