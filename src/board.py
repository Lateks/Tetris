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

    def __get_block_repr_if_exists_at(self, position):
        block = self.__get_block_at(position)
        return str(block) if block else None

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
        if self.__no_falling_blocks():
            raise IllegalStateException('Cannot tick, no blocks falling.')
        falling_block = self.blocks[0]
        x, y = falling_block.get_position()
        if self.__is_last_row(y) or self.__contains_a_block((x, y + 1)):
            self.has_falling = False
        else:
            falling_block.set_position((x, y + 1))

    def __no_falling_blocks(self):
        return not self.has_falling

    def __is_last_row(self, row):
        return row == self.rows - 1

    def __contains_a_block(self, position):
        if self.__get_block_at(position):
            return True
        else:
            return False

    def __get_block_at(self, position):
        for block in self.blocks:
            if block.is_at_position(position):
                return block
        return None
