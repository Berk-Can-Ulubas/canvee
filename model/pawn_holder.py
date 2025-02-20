class Holder:
    def __init__(self, next_holder):
        self.pawn = None
        self.next_holder = next_holder
        self.name = None
    
    def __init__(self):
        self.pawn = None
        self.next_holder = None
        self.name = None


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
    
    def get_pawn(self):
        return self.pawn
    
    def get_next_holder(self):
        return self.next_holder
    
    def set_next_holder(self, next_holder):
        if not isinstance(next_holder, Holder): 
            raise ValueError("Next holder must be an instance of the Holder class.")
        self.next_holder = next_holder