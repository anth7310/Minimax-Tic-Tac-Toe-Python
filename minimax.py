class Board:
    def __init__(self):
        """
        3x3 tic tac toe Board is represented as a list
        """
        self.board = [None]*9

    def assign(self, index, player):
        """
        Assign player to index
        """
        self.board[index] = player
    
    def deassign(self, index):
        """
        Remove player from index
        """
        self.board[index] = None

    def calculateWinner(self):
        """
        Return winner
        """
        winner = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5 ,8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        board = self.board
        for a, b, c in winner:
            if board[a] == board[b] == board[c] and board[a] != None:
                return board[a]
        if None not in board:
            return 'tie'

    def __str__(self):
        return (
            str(self.board[:3]) + '\n' +
            str(self.board[3:6]) + '\n' +
            str(self.board[6:])
        )
        # return str(self.board)


def minimax(board, player):
    """ Minimax algorithm on Tic Tac Toe 
    """
    result = board.calculateWinner()
    if result == 'x':
        return 1
    elif result == 'o':
        return -1
    elif result == 'tie':
        return 0

    # return if can win within next move
    for idx, square in enumerate(board.board):
        if square == None:
            board.assign(idx, player)
            if board.calculateWinner() == player:
                board.deassign(idx)
                return idx
            board.deassign(idx)

    root = []
    for idx, square in enumerate(board.board):
        if square == None:
            board.assign(idx, player)
            root.append(minimax(board, player='x' if player=='o' else 'o'))
            board.deassign(idx)
        else: # to maintain root length
            root.append(0)

    # unfilled spots in board
    unfilled = [ i for i, v in enumerate(root) if (board.board[i] == None)]
    # select optimal index from unfilled
    d = { root[k]: v for k, v in enumerate(unfilled) }
    print(d)
    if player == 'x':
        return d[max(d)]
    else:
        return d[min(d)]

def alpha_Beta(board, player, alpha, beta):
    """ Minimax algorithm on Tic Tac Toe with minimax pruning
    """
    if board.calculateWinner() == 'x':
        return 1
    elif board.calculateWinner() == 'o':
        return -1
    elif board.calculateWinner() == 'tie':
        return 0

    # check if can win within next move
    for idx, square in enumerate(board.board):
        if square == None:
            board.assign(idx, player)
            if board.calculateWinner() == player:
                board.deassign(idx)
                return idx
            board.deassign(idx)

    root = []
    if player == 'x':
        value = -float("Inf")
        for idx, square in enumerate(board.board):
            if square == None:
                board.assign(idx, player)
                
                value = max(value, alpha_Beta(board, player='o', alpha=alpha, beta=beta))
                alpha = max(alpha, value)
                board.deassign(idx)
                root.append(value)
                if alpha >= beta: # cut off beta
                    break
            else: # to maintain root length
                root.append(0)
        return root.index(max(root))
        
    else:
        value = float("Inf")
        for idx, square in enumerate(board.board):
            if square == None:
                board.assign(idx, player)
                
                value = min(value, alpha_Beta(board, player='x', alpha=alpha, beta=beta))
                beta = min(beta, value)
                board.deassign(idx)
                root.append(value)
                if alpha >= beta: # cut off alpha
                    break
            else: # to maintain root length
                root.append(0)
        return root.index(min(root))


"""
x | o |
o | x | 
  |   |
"""
# game = Board()
# game.assign(0, 'x')
# game.assign(1, 'o')
# game.assign(4, 'x')
# game.assign(3, 'o')
# print(game)
# x = alpha_Beta(game, player='x', alpha=-float('Inf'), beta=float("Inf"))
# print(x)


## Play Game
game = Board()
while True:
    print(game)
    x = int(input())
    game.assign(x, 'x')
    print(game)
    o = minimax(game, player='o')
    game.assign(o, 'o')
    