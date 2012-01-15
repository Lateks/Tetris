from math import floor
from exception import IllegalStateException

class Board:
    empty_tile = '.'

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.has_falling = False
        self.blocks = list()

    def __str__(self):
        representation = ''
        for y in range(0, self.rows):
            for x in range(0, self.columns):
                representation += self.__get_block_repr_or_empty_tile_at((x, y))
            representation += '\n'
        return representation

    def __get_block_repr_or_empty_tile_at(self, position):
        block = self.__get_block_at(position)
        return str(block) if block else self.empty_tile

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
        self.__move_down_one_row_or_stop(falling_block)

    def __no_falling_blocks(self):
        return not self.has_falling

    def __move_down_one_row_or_stop(self, block):
        x, y = block.get_position()
        new_row = y + 1
        if self.__block_should_stop_falling_at((x, y)):
            self.has_falling = False
        else:
            block.set_position((x, new_row))

    def __block_should_stop_falling_at(self, position):
        x, y = position
        block_on_last_row = self.__is_last_row(y)
        block_on_top_of_a_block = self.__contains_a_block((x, y + 1))
        return block_on_last_row or block_on_top_of_a_block

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
