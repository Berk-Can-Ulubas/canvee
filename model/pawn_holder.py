class Holder:
    def __init__(self, next_holder):
        self.pawn = None
        self.next_holder = next_holder

    def add_pawn(self, pawn):
        if self.pawn is None:
            self.pawn = pawn
        else:
            raise ValueError("Space is already occupied")

    def remove_pawn(self, pawn):
        if self.pawn == pawn:
            self.pawn = None
        else:
            raise ValueError("Pawn not in this space")

    def is_empty(self):
        return self.pawn is None