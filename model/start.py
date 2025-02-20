from model.color import Color
from model.pawn_holder import Holder


class Start(Holder):
    def __init__(self, color):
        super().__init__()
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of the Color Enum.")
        self.color = color
        super.name = f'start {self.color}'
