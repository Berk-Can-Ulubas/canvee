class Pawn:
    def __init__(self, color):
        # Überprüfen, dass color ein Color Enum ist
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of the Color Enum.")
        
        self.color = color
        self.position = None

    def move(self, position):
        if not isinstance(position, Holder):
            raise ValueError("Position must be an instance of the Holder class.")
         
        self.position = position

    def __str__(self):
        return f'{self.color} pawn at {self.position}'