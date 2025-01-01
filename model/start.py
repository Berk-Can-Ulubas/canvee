class Start(space):
    def __init__(self, color):
        super().__init__()
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of the Color Enum.")
        self.color = color
