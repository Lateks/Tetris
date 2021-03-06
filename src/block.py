class Block(object):
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return self.type

    def move_to(self, (x, y)):
        self.position = (x, y)

    def get_position(self):
        return self.position

    def is_at_position(self, (x, y)):
        return self.position == (x, y)

    def move_down(self):
        self.move_relative_to_original_position(0, 1)

    def move_relative_to_original_position(self, x, y):
        orig_x, orig_y = self.position
        self.position = (orig_x + x, orig_y + y)
