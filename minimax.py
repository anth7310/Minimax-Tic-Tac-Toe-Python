def checkWinner(board):
    """ Returns true if winner exist
    """
    states = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5 ,8],
            [0, 4, 8],
            [2, 4, 6]
        ]
    # flatten board
    flat_board = [] 
    for row in board:
        for col in row:
            flat_board.append(col)

    # No empty states, return tie
    if '' not in flat_board:
        return 'tie'

    # Winner exist
    for state in states:
        a, b, c = state
        if flat_board[a] == flat_board[b] == flat_board[c] and flat_board[a] != '':
            return flat_board[a]

    # Game still continuing
    return ''
       

def minimax(board, depth, isMax):
    """
    Takes a 3x3 list
    depth is recursion depth
    isMax is maximizing player
    """
    bestMove = []
    result = checkWinner(board)
    if result == 'x': # heristic values
        return 10
    if result == 'o':
        return -10
    if result == 'tie':
        return 0
    if isMax: # maximizing player is 'x'
        bestScore = -float("Inf")
        if result == '': # is there empty spot to play
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'x'
                        # add depth to optimize play, want player to choose fastest win
                        value = minimax(board, depth+1, False) - depth
                        board[i][j] = ''
                        bestScore = max(bestScore, value)
                        
    else: # minimizing player is 'o'
        bestScore = float("Inf")
        if result == '':
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'o'
                        value = minimax(board, depth+1, True) + depth
                        board[i][j] = ''
                        bestScore = min(bestScore, value)
    # return the best score for the given board
    return bestScore

def calculateScores(board, isMax):
    # calculate values with heuristic score
    scores = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
        ]
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                if isMax:
                    board[i][j] = 'x'
                    scores[i][j] = minimax(board, 0, not isMax)
                else:
                    board[i][j] = 'o'
                    scores[i][j] = minimax(board, 0, not isMax)
                board[i][j] = ''
    return scores

def pickOptimalMove(board, isMax, returnScore=False):
    
    if isMax:
        bestScore = -float("Inf") 
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'x'
                    score = minimax(board, 0, False)
                    board[i][j] = ''
                    if score > bestScore:
                        bestScore = score
                        bestMove = (i, j)
                    
    else:
        bestScore = float("Inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'o'
                    score = minimax(board, 0, True)
                    board[i][j] = ''
                    if score < bestScore:
                        bestScore = score
                        bestMove = (i, j)
                
    if returnScore:
        return bestMove, bestScore
    return bestMove
    
# board = [
#     ['x', 'x', ''],
#     ['', 'o', ''],
#     ['', '', 'o']
# ]

board = [
    ['', 'o', 'x'],
    ['o', 'x', ''],
    ['', '', '']
] # (2, 0)

# board = [
#     ['x', 'o', ''],
#     ['o', 'x', ''],
#     ['', '', '']
# ] # (2, 2)

# board = [
#     ['x', 'o', ''],
#     ['x', 'o', ''],
#     ['', '', '']
# ] (2, 0)

# board = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]

print(minimax(board, 0, isMax=True))
print(calculateScores(board, True))
print(pickOptimalMove(board, isMax=True, returnScore=False))

### Play game
# while True:
#     print(calculateScores(board, isMax=True))
#     ai = pickOptimalMove(board, isMax=True, returnScore=False)
#     board[ai[0]][ai[1]] = 'x'
#     print(board)

#     x = int(input())
#     y = int(input())
#     board[x][y] = 'o'
#     print(board)

