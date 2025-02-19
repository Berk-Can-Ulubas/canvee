class Space(Holder):
    def __init__(self, next_holder):
        super().__init__(next_holder)
        self.name = "Space " + str(id(self))

    def id()