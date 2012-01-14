class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.has_falling = False

    def __str__(self):
        representation = ''
        if self.has_falling:
            return ".X.\n" + 2 * "...\n"
        for i in range(0, self.rows):
            for i in range(0, self.columns):
                representation += '.'
            representation += '\n'
        return representation

    def has_falling_blocks(self):
        return self.has_falling

    def drop(self, block):
        self.has_falling = True
