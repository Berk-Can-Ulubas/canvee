class Base:
    def __init__(self):
        self.pawns = []

    def add_pawn(self, pawn):
        if not isinstance(pawn, Pawn):
            raise ValueError("Pawn must be an instance of the Pawn class.")
        
        self.pawns.append(pawn)

    def remove_pawn(self, pawn):
        if not isinstance(pawn, Pawn):
            raise ValueError("Pawn must be an instance of the Pawn class.")
        
        self.pawns.remove(pawn)

    def is_empty(self):
        return len(self.pawns) == 0