class Block:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return self.type

    def set_position(self, (x, y)):
        self.position = (x, y)

    def get_position(self):
        return self.position

    def is_at_position(self, (x, y)):
        return self.position == (x, y)
