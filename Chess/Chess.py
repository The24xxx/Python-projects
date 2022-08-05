class Chess():
    """
    Game rules, whose turn it is etc.
    """
    
    def __init__(self):
        
        pass
    
    def promotion(self):
       
        pass
    
    def move(self):
        
        pass

class Board():
    """
    The configuration of the board, where the pieces are.
    """
    
    def __init__(self):
        
        pass
    
    def print_board(self):
        
        pass
    
class Piece():
    """
    Pieces - types, moves, colour.
    """

    def __init__(self):

        pass
    
    def is_valid_move(self):

        pass
    
    def is_white(self):

        pass

    def __str__(self):
        return ''

class Rook(Piece):
    def __init__(self, colour):
        pass
    
    def is_valid_move(self, board, start, to):
        pass

class Bishop(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

class Knight(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

class  Queen(Piece):
    def __init__(self):
        pass
   
    def is_valid_move(self):
        pass

class King (Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass

# Class to represent a pseudo pawn that can be taken when en passant is possible

class GhostPawn(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        return False

class Pawn(Piece):
    def __init__(self):
        pass

    def is_valid_move(self):
        pass