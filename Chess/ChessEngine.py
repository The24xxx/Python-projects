# This class is responsible for storing all the information about current state of chess game. It will also be responsible
# for determining the valid moves at the current state. It will also keep move log.

class GameState():
    def __init__(self):
        # The board is 8x8 2D list, each element of the list has 2 characters.
        # The first character represents the color of the piece: 'b' ir 'w'
        # The second characters represents the type of the piece: 'K', 'Q', 'R', 'B', 'N', or 'p'
        # '--' represents white space with no piece.
        self.board = [
            ["bR","bN", "bB", "bQ", "bK", "bB", "bN", "bR" ],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR","wN", "wB", "wQ", "wK", "wB", "wN", "wR" ]]
        
        self.whiteToMove = True
        self.moveLog = []
    '''
    Takes a Move as a parameter and executes it (it will not work for castling, pawn promotion, and en-passant)
    '''
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) #log the move so we can undo it later
        self.whiteToMove = not self.whiteToMove #swap players

    '''
    Undo the last move made
    '''

    def undoMove(self):
        if len(self.moveLog) != 0: #make sure that there is a move to undo
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove #switch turns back

    '''
    All moves considering checks
    '''
    def getValidMoves(self):
        return self.getAllPossibleMoves() #for now to not worry about checks


    '''
    All moves without considering checks
    '''
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)): #num of rows
            for c in range(len(self.board[r])): #num of columns in given row
                turn = self.board[r][c][0] #first character on square (b, w or) - represents color or empty field
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnMoves(r, c, moves)
                    if piece == 'R':
                        self.getRookMoves(r, c, moves)
                    if piece == 'N':
                        self.getKnightMoves(r, c, moves)
                    if piece == 'B':
                        self.getBishopMoves(r, c, moves)
                    if piece == 'Q':
                        self.getQueenMoves(r, c, moves)
                    if piece == 'K':
                        self.getKingMoves(r, c, moves)

    '''
    Get all the piece moves for the piece located at row, col and add these moves to the list
    '''
    def getPawnMoves(self, r, c, moves):
        pass
    def getRookMoves(self, r, c, moves):
        pass
    def getKnightMoves(self, r, c, moves):
        pass
    def getBishopMoves(self, r, c, moves):
        pass
    def getQueenMoves(self, r, c, moves):
        pass
    def getKingMoves(self, r, c, moves):
        pass
    


class Move():
    # maps keys to values - translate python coordinations to chess game coordinations
    # key = value
    rankToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in rankToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}


    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]


    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]