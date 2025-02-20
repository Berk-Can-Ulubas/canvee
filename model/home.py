from model.color import Color
from model.pawn_holder import Holder

class Home(Holder):
    def __init__(self, next_holder, color, index):
        super().__init__(next_holder)
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of the Color Enum.")
        self.color = color
        if not isinstance(index, int):
            raise ValueError("Index must be an integer.")
        super.name = f' home {index} {self.color}'

    def __init__(self, color, index):
        super().__init__()
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of the Color Enum.")
        self.color = color
        if not isinstance(index, int):
            raise ValueError("Index must be an integer.")
        super.name = f' home {index} {self.color}'

    def get_color(self):
        return self.color