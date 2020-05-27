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
        return str(self.board)


def minimax(board, player):
    if board.calculateWinner() == 'x':
        return 1
    elif board.calculateWinner() == 'o':
        return -1
    elif board.calculateWinner() == 'tie':
        return 0

    root = []
    for idx, square in enumerate(board.board):
        if square == None:
            board.assign(idx, player)
            root.append(minimax(board, player='x' if player=='o' else 'o'))
            board.deassign(idx)
        else: # to maintain root length
            root.append(0)
    if player == 'x':
        return root.index(max(root))
    else:
        return root.index(min(root))

game = Board()
game.assign(0, 'x')
game.assign(1, 'o')
game.assign(3, 'x')
game.assign(2, 'o')
x = minimax(game, player='x')
print(x)
print(game)