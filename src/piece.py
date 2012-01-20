from block import Block

class Piece(object):
    def __init__(self, piece_repr):
        self.piece = piece_repr.split('\n')
        if self.piece[-1] == '':
            self.piece.pop(-1)
        self.__init_blocks()

    def __init_blocks(self):
        self.blocks = list()
        row_mid = len(self.piece[0])/2
        row_offset = self.__first_non_empty_row()
        for row in range(0, len(self.piece)):
            for col in range(0, len(self.piece[row])):
                block_symbol = self.piece[row][col]
                if block_symbol != '.':
                    block = Block(block_symbol)
                    block.move_to((col - row_mid, row - row_offset))
                    self.blocks.append(block)

    def __first_non_empty_row(self):
        for row in range(0, len(self.piece)):
            if self.__row_non_empty(row):
                return row

    def __row_non_empty(self, row):
        for block_symbol in self.piece[row]:
            if block_symbol != '.':
                return True
        return False

    def __str__(self):
        return self.__concatenate_rows_to_string(self.piece)

    def move_down(self):
        for block in self.blocks:
            block.move_down()

    def move_relative_to_original_position(self, (x, y)):
        for block in self.blocks:
            block.move_relative_to_original_position(x, y)

    def rotate_right(self):
        ordered_rows, ordered_cols = self.__right_rotation_params()
        rotated_piece = self.__rotate_piece(ordered_rows, ordered_cols)
        rotated_piece_repr = self.__concatenate_rows_to_string(rotated_piece)
        return Piece(rotated_piece_repr)

    def rotate_left(self):
        ordered_rows, ordered_cols = self.__left_rotation_params()
        rotated_piece = self.__rotate_piece(ordered_rows, ordered_cols)
        rotated_piece_repr = self.__concatenate_rows_to_string(rotated_piece)
        return Piece(rotated_piece_repr)

    def __right_rotation_params(self):
        rows = cols = len(self.piece)
        ordered_rows = self.__true_reverse_list(range(0, rows))
        ordered_cols = range(0, cols)
        return ordered_rows, ordered_cols

    def __left_rotation_params(self):
        rows = cols = len(self.piece)
        ordered_rows = range(0, rows)
        ordered_cols = self.__true_reverse_list(range(0, cols))
        return ordered_rows, ordered_cols

    def __true_reverse_list(self, list_to_reverse):
        return list(reversed(list_to_reverse))

    def __rotate_piece(self, ordered_rows, ordered_columns):
        rotated_piece = list()
        for col in ordered_columns:
            new_row = ''
            for row in ordered_rows:
                new_row += self.piece[row][col]
            rotated_piece.append(new_row)
        return rotated_piece

    def __concatenate_rows_to_string(self, rows):
        representation = ''
        for row in rows:
            representation += row + '\n'
        return representation

    def __iter__(self):
        for block in self.blocks:
            yield block
