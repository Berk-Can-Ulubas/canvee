class Holder:
    def add_pawn(self, pawn):
        self.pawn = pawn

    def remove_pawn(self, pawn):
        self.pawn = None

    def is_empty(self):
        return self.pawn is None