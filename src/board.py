class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def __str__(self):
        representation = ''
        for i in range(0, self.rows):
            for i in range(0, self.columns):
                representation += '.'
            representation += '\n'
        return representation

    def has_falling_blocks(self):
        return False
