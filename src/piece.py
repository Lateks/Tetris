class Piece:
    def __init__(self, piece_repr):
        self.piece = piece_repr.split('\n')
        self.piece.pop(-1)

    def __str__(self):
        return self.__concatenate_rows_to_string(self.piece)

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
