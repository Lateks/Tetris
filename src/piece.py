class Piece:
    def __init__(self, piece_repr):
        self.piece_repr = piece_repr.split('\n')
        self.piece_repr.pop(-1)

    def __str__(self):
        return self.__concatenate_rows_with_newlines(self.piece_repr)

    def rotate_right(self):
        rows = cols = len(self.piece_repr)
        new_piece_repr = list()
        for col in range(0, cols):
            new_row_repr = ''
            for row in reversed(range(0, rows)):
                new_row_repr += self.piece_repr[row][col]
            new_piece_repr.append(new_row_repr)
        return Piece(self.__concatenate_rows_with_newlines(new_piece_repr))

    def __concatenate_rows_with_newlines(self, repr_rows):
        representation = ''
        for row in repr_rows:
            representation += row + '\n'
        return representation
