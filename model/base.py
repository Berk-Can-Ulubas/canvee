class Base:
    def __init__(self, color):
        self.pawns = []
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of the Color Enum.")
        self.color = color

    def add_pawn(self, pawn):
        if not isinstance(pawn, Pawn):
            raise ValueError("Pawn must be an instance of the Pawn class.")
        if len(self.pawns) >= 4:
            raise ValueError("A base can only hold up to 4 pawns.")
        self.pawns.append(pawn)

    def remove_pawn(self, pawn):
        if not isinstance(pawn, Pawn):
            raise ValueError("Pawn must be an instance of the Pawn class.")
        self.pawns.remove(pawn)

    def is_empty(self):
        return len(self.pawns) == 0
    
    def __str__(self):
        return f'{self.color} base with {len(self.pawns)} pawns: {self.pawns}'