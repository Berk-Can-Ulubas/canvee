from model.pawn_holder import Holder


class Space(Holder):
    def __init__(self, next_holder, index):
        super().__init__(next_holder)
        if not isinstance(index, int):
            raise ValueError("Index must be an integer.")
        super.name = "Space " + str(index)

    def __init__(self, index):
        super().__init__()
        if not isinstance(index, int):
            raise ValueError("Index must be an integer.")
        super.name = "Space " + str(index)