board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

compPiece = 'O'
piece = 'X'

def printBoard():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    return

def checkWin(piece):
    if board[1] == board[2] == board[3] == piece:
        return True
    elif board[4] == board[5] == board[6] == piece:
        return True
    elif board[7] == board[8] == board[9] == piece:
        return True
    elif board[1] == board[4] == board[7] == piece:
        return True
    elif board[2] == board[5] == board[8] == piece:
        return True
    elif board[3] == board[6] == board[9] == piece:
        return True
    elif board[1] == board[5] == board[9] == piece:
        return True
    elif board[3] == board[5] == board[7] == piece:
        return True
    return False

def checkFree(pos):
    if board[pos] == ' ':
        return True
    return False

def computerMove():
    bestScore = -1000
    bestMove = 0
    for i in range(1,10):
        if checkFree(i):
            board[i] = compPiece
            score = minimax(board, False)
            board[i] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = i
    board[bestMove] = compPiece
    return

def minimax(board, isMaximizing):
    if checkWin(compPiece):
        return 1
    elif checkWin(piece):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1000
        for i in range(1,10):
            if checkFree(i):
                board[i] = compPiece
                score = minimax(board, False)
                board[i] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 1000
        for i in range(1,10):
            if checkFree(i):
                board[i] = piece
                score = minimax(board, True)
                board[i] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore

def checkDraw():
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True

printBoard()
while not(checkDraw()) and not(checkWin(compPiece) and not(checkWin(piece))):

    position = int(input("Please make your move: "))
    while not(checkFree(position)):
        position = int(input("Please make your move: "))
    board[position] = piece
    computerMove()
    printBoard()
    if checkWin(compPiece):
        print("Computer wins")
    elif checkWin(piece):
        print("Player wins")
    elif checkDraw():
        print("draw.")
