from piece import Piece

class Tetrominoe(Piece):
    def __init__(self, shape_repr, max_rotations, current_rotation):
        super(Tetrominoe, self).__init__(shape_repr)
        self.current_rotation = current_rotation
        self.max_rotations = max_rotations
        self.original = self.__original_rotation()

    def __original_rotation(self):
        if self.current_rotation == 0:
            return str(self)
        elif self.current_rotation > 0:
            rotation = self.__rotate_piece_left(self.current_rotation)
            return str(rotation)
        else:
            rotation = self.__rotate_piece_right(abs(self.current_rotation))
            return str(rotation)

    def __rotate_piece_left(self, times):
        rotation = super(Tetrominoe, self).rotate_left()
        for i in range(1, times):
            rotation = rotation.rotate_left()
        return rotation

    def __rotate_piece_right(self, times):
        rotation = super(Tetrominoe, self).rotate_right()
        for i in range(1, times):
            rotation = rotation.rotate_right()
        return rotation

    def rotate_left(self):
        if -self.current_rotation == self.max_rotations:
            return Tetrominoe(self.original, self.max_rotations, 0)
        else:
            rotated = super(Tetrominoe, self).rotate_left()
            rotation = self.current_rotation - 1
            return Tetrominoe(str(rotated), self.max_rotations, rotation)

    def rotate_right(self):
        if self.current_rotation == self.max_rotations:
            return Tetrominoe(self.original, self.max_rotations, 0)
        else:
            rotated = super(Tetrominoe, self).rotate_right()
            rotation = self.current_rotation + 1
            return Tetrominoe(str(rotated), self.max_rotations, rotation)

T_SHAPE = Tetrominoe(".T.\n" + \
                     "TTT\n" + \
                     "...\n", 3, 0)

I_SHAPE = Tetrominoe(".....\n" + \
                     ".....\n" + \
                     "IIII.\n" + \
                     ".....\n" + \
                     ".....\n", 1, 0)

O_SHAPE = Tetrominoe(".OO\n" + \
                     ".OO\n" + \
                     "...\n", 0, 0)

L_SHAPE = Tetrominoe("...\n" + \
                     "LLL\n" + \
                     "L..\n", 3, 0)

J_SHAPE = Tetrominoe("...\n" + \
                     "JJJ\n" + \
                     "..J\n", 3, 0)

Z_SHAPE = Tetrominoe("...\n" + \
                     "ZZ.\n" + \
                     ".ZZ\n", 1, 0)

S_SHAPE = Tetrominoe("...\n" + \
                     ".SS\n" + \
                     "SS.\n", 1, 0)
