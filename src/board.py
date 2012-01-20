from math import floor
from exception import IllegalStateException

class Board(object):
    empty_tile = '.'

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.has_falling = False
        self.blocks = list()
        self.falling_piece = None

    def __str__(self):
        representation = ''
        for y in range(0, self.rows):
            for x in range(0, self.columns):
                representation += self.__get_block_repr_or_empty_tile_at((x, y))
            representation += '\n'
        return representation

    def __get_block_repr_or_empty_tile_at(self, position):
        block = self.__get_block_at(position)
        block = block if block else self.__get_falling_piece_block_at(position)
        return str(block) if block else self.empty_tile

    def has_falling_pieces(self):
        return self.has_falling

    def drop(self, piece):
        if self.has_falling:
            raise IllegalStateException(
                'Only one piece may be falling at a time.')
        self.__position(piece)
        self.falling_piece = piece
        self.has_falling = True

    def __position(self, piece):
        x, y = int((self.columns / 2)), 0
        piece.move_relative_to_original_position((x, y))

    def tick(self):
        if self.__no_falling_pieces():
            raise IllegalStateException('Cannot tick, no pieces falling.')
        self.__falling_piece_down_one_row_or_stop()

    def __no_falling_pieces(self):
        return not self.has_falling

    def __falling_piece_down_one_row_or_stop(self):
        if self.__piece_should_stop_falling():
            self.has_falling = False
            for block in self.falling_piece:
                self.blocks.append(block)
            self.falling_piece = None
        else:
            self.falling_piece.move_down()

    def __piece_should_stop_falling(self):
        for block in self.falling_piece:
            x, y = block.get_position()
            block_on_last_row = self.__is_last_row(y)
            block_on_top_of_a_block = self.__contains_a_block((x, y + 1))
            if block_on_last_row or block_on_top_of_a_block:
                return True
        return False

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

    def __get_falling_piece_block_at(self, position):
        if self.__no_falling_pieces():
            return None
        for block in self.falling_piece:
            if block.is_at_position(position):
                return block
        return None
