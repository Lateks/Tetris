from piece import Piece

class Tetrominoe(Piece):
    def __init__(self, shape_repr):
        super(Tetrominoe, self).__init__(shape_repr)

T_SHAPE = Tetrominoe(".T.\n" + \
                     "TTT\n" + \
                     "...\n")
