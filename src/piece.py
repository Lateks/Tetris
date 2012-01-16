class Piece:
    def __init__(self, piece_repr):
        self.piece = piece_repr.split('\n')
        self.piece.pop(-1)

    def __str__(self):
        return self.__concatenate_rows_to_string(self.piece)

    def rotate_right(self):
        rows = cols = len(self.piece)
        rotated_piece = list()
        for col in range(0, cols):
            new_row = ''
            for row in reversed(range(0, rows)):
                new_row += self.piece[row][col]
            rotated_piece.append(new_row)
        rotated_piece_repr = self.__concatenate_rows_to_string(rotated_piece)
        return Piece(rotated_piece_repr)

    def rotate_left(self):
        rows = cols = len(self.piece)
        rotated_piece = list()
        for col in reversed(range(0, cols)):
            new_row = ''
            for row in range(0, cols):
                new_row += self.piece[row][col]
            rotated_piece.append(new_row)
        rotated_piece_repr = self.__concatenate_rows_to_string(rotated_piece)
        return Piece(rotated_piece_repr)

    def __concatenate_rows_to_string(self, rows):
        representation = ''
        for row in rows:
            representation += row + '\n'
        return representation
