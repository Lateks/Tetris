from math import floor
from exception import IllegalStateException

class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.has_falling = False
        self.blocks = list()

    def __str__(self):
        representation = ''
        for y in range(0, self.rows):
            for x in range(0, self.columns):
                block_repr = self.__get_block_repr_if_exists_at((x, y))
                representation += block_repr if block_repr else '.'
            representation += '\n'
        return representation

    def __get_block_repr_if_exists_at(self, (x, y)):
        for block in self.blocks:
            if block.is_at_position((x, y)):
                block_repr = str(block)
                return block_repr
        return None

    def has_falling_blocks(self):
        return self.has_falling

    def drop(self, block):
        if self.has_falling:
            raise IllegalStateException(
                'Only one block may be falling at a time.')
        self.__new_block(block)
        self.has_falling = True

    def __new_block(self, block):
        self.blocks.insert(0, block)
        x, y = int(floor(self.columns / 2)), 0
        block.set_position((x, y))

    def tick(self):
        falling_block = self.blocks[0]
        x, y = falling_block.get_position()
        if self.__is_last_row(y):
            self.has_falling = False
        else:
            falling_block.set_position((x, y + 1))

    def __is_last_row(self, row):
        return row == self.rows - 1
