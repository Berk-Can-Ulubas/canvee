class HomeColumn:
    def __init__(self, color):
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of the Color Enum.")
        self.color = color
        self.pawns = [4]

    def add_pawn(self, pawn, index):
        if not isinstance(pawn, Pawn):
            raise ValueError("Pawn must be an instance of the Pawn class.")
        if len(self.pawns) >= 4:
            raise ValueError("A home column can only hold up to 4 pawns.")
        if index not in range(0, 4):
            raise ValueError("Index must be between 0 and 3.")
        self.pawns[index] = pawn


    def move_pawn(self, pawn, steps):

    def is_empty(self):
        return self.pawns == [None, None, None, None]