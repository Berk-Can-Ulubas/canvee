from model.color import Color
from model.pawn_holder import Holder

class Home(Holder):
    def __init__(self, next_holder, color):
        super().__init__(next_holder)
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of the Color Enum.")
        self.color = color

    def get_color(self):
        return self.color