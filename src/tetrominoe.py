from piece import Piece

class Tetrominoe(Piece):
    def __init__(self, shape_repr):
        super(Tetrominoe, self).__init__(shape_repr)

T_SHAPE = Tetrominoe(".T.\n" + \
                     "TTT\n" + \
                     "...\n")

I_SHAPE = Tetrominoe(".....\n" + \
                     ".....\n" + \
                     "IIII.\n" + \
                     ".....\n" + \
                     ".....\n")

O_SHAPE = Tetrominoe(".OO\n" + \
                     ".OO\n" + \
                     "...\n")

L_SHAPE = Tetrominoe("...\n" + \
                     "LLL\n" + \
                     "L..\n")

J_SHAPE = Tetrominoe("...\n" + \
                     "JJJ\n" + \
                     "..J\n")

Z_SHAPE = Tetrominoe("...\n" + \
                     "ZZ.\n" + \
                     ".ZZ\n")

S_SHAPE = Tetrominoe("...\n" + \
                     ".SS\n" + \
                     "SS.\n")
