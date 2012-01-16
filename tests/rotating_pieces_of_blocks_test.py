import unittest
from src.piece import Piece

class RotatingPiecesOfBlocksTestSuiteGenerator:
    def __init__(self):
        self.loader = unittest.TestLoader()

    def suite(self):
        piece3x3 = self.a_piece_of_3x3_blocks_suite()
        return piece3x3

    def a_piece_of_3x3_blocks_suite(self):
        return self.loader.loadTestsFromTestCase(APieceOf3x3Blocks)

    #def a_piece_of_5x5_blocks_suite(self):
    #    return self.loader.loadTestsFromTestCase(APieceOf5x5Blocks)

class APieceOf3x3Blocks(unittest.TestCase):
    def setUp(self):
        self.piece_repr = ".X.\n" + \
                          ".X.\n" + \
                          "...\n"
        self.piece = Piece(self.piece_repr)

    def test_consists_of_many_blocks(self):
        self.assertEqual(self.piece_repr, str(self.piece))

    def test_can_be_rotated_right(self):
        piece = self.piece.rotate_right()
        expected_piece = "...\n" + \
                         ".XX\n" + \
                         "...\n"
        self.assertEqual(expected_piece, str(piece))

    def test_can_be_rotated_left(self):
        piece = self.piece.rotate_left()
        expected_piece = "...\n" + \
                         "XX.\n" + \
                         "...\n"
        self.assertEqual(expected_piece, str(piece))

#class APieceOf3x3Blocks(unittest.TestCase):
#    def setUp(self):
#        self.piece_repr = "..XXX\n" +
#                          "..XX.\n" +
#                          "..X..\n" +
#                          ".....\n" +
#                          ".....\n"
#        self.piece = Piece(piece_repr)
#
#    def test_consists_of_many_blocks(self):
#        assertEqual(self.piece_repr, str(self.piece))
#
#    def test_can_be_rotated_right(self):
#        self.piece = self.piece.rotate_right()
#        expected_piece = ".....\n" +
#                         ".....\n" +
#                         "..XXX\n" +
#                         "...XX\n" +
#                         "....X\n"
#        assertEqual(expected_piece, str(self.piece))
#
#    def test_can_be_rotated_left(self):
#        self.piece = self.piece.rotate_left()
#        expected_piece = "X....\n" +
#                         "XX...\n" +
#                         "XXX..\n" +
#                         ".....\n" +
#                         ".....\n"
#        assertEqual(expected_piece, str(self.piece))
