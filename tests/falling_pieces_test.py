import unittest
import src.tetrominoe as tetrominoe
from src.board import Board

class FallingPiecesTestSuiteGenerator:
    def __init__(self):
        self.loader = unittest.TestLoader()

    def suite(self):
        piece_dropped = self.when_a_piece_is_dropped_suite()
        return piece_dropped

    def when_a_piece_is_dropped_suite(self):
        return self.loader.loadTestsFromTestCase(WhenAPieceIsDropped)

class WhenAPieceIsDropped(unittest.TestCase):
    def setUp(self):
        self.board = Board(6, 8)

    def test_t_shape_starts_from_top_middle(self):
        self.board.drop(tetrominoe.T_SHAPE)
        self.assertEqual("....T...\n" + \
                         "...TTT..\n" + \
                         "........\n" + \
                         "........\n" + \
                         "........\n" + \
                         "........\n", str(self.board))

    def test_o_shape_starts_from_top_middle(self):
        self.board.drop(tetrominoe.O_SHAPE)
        self.assertEqual("...OO...\n" + \
                         "...OO...\n" + \
                         "........\n" + \
                         "........\n" + \
                         "........\n" + \
                         "........\n", str(self.board))

    def test_i_shape_starts_from_top_middle(self):
        self.board.drop(tetrominoe.I_SHAPE)
        self.assertEqual("..IIII..\n" + \
                         "........\n" + \
                         "........\n" + \
                         "........\n" + \
                         "........\n" + \
                         "........\n", str(self.board))

    def test_l_shape_starts_from_top_middle(self):
        self.board.drop(tetrominoe.L_SHAPE)
        self.assertEqual("...LLL..\n" + \
                         "...L....\n" + \
                         "........\n" + \
                         "........\n" + \
                         "........\n" + \
                         "........\n", str(self.board))

#class WhenAPieceReachesTheBottom(unittest.TestCase):
#    def setUp(self):
#        self.board = Board(6, 8)
#        self.board.drop(tetrominoe.T_SHAPE)
#        for i in range(0, 4)
#        self.board.tick()
#
#    def test_piece_is_still_falling_on_the_last_row(self):
#        self.assertTrue(self.board.has_falling_blocks())
#        self.assertEqual("........\n" + \
#                         "........\n" + \
#                         "........\n" + \
#                         "........\n" + \
#                         "....T...\n" + \
#                         "...TTT..\n", str(self.board))
#
#    def test_piece_stops_when_it_hits_the_bottom(self):
#        self.board.tick()
#        self.assertFalse(self.board.has_falling_blocks())
#        self.assertEqual("........\n" + \
#                         "........\n" + \
#                         "........\n" + \
#                         "........\n" + \
#                         "....T...\n" + \
#                         "...TTT..\n", str(self.board))
#
#class WhenAPieceLandsOnAnotherPiece(unittest.TestCase):
#    def setUp(self):
#        self.board = Board(6, 8)
#        self.board.drop(tetrominoe.T_SHAPE)
#        for i in range(0, 5):
#            self.board.tick()
#        self.board.drop(tetrominoe.T_SHAPE)
#        self.board.tick()
#        self.board.tick()
#
#    def test_piece_is_still_falling_right_above_the_other_piece(self):
#        self.assertTrue(self.board.has_falling_blocks())
#        self.assertEqual("........\n" + \
#                         "........\n" + \
#                         "....T...\n" + \
#                         "...TTT..\n" + \
#                         "....T...\n" + \
#                         "...TTT..\n", str(self.board))
#
#    def test_piece_stops_when_it_hits_the_other_piece(self):
#        self.board.tick()
#        self.assertFalse(self.board.has_falling_blocks())
#        self.assertEqual("........\n" + \
#                         "........\n" + \
#                         "....T...\n" + \
#                         "...TTT..\n" + \
#                         "....T...\n" + \
#                         "...TTT..\n", str(self.board))
