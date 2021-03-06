import unittest
from src.board import Board
from src.piece import Piece
from src.block import Block
from src.exception import IllegalStateException

class FallingBlockTestSuiteGenerator:
    def __init__(self):
        self.loader = unittest.TestLoader()

    def suite(self):
        a_new_board = self.new_board_suite()
        block_dropped = self.when_a_block_is_dropped_suite()
        block_reaches_bottom = self.when_a_block_reaches_the_bottom_suite()
        block_lands_on_another = self.block_lands_on_another()
        return unittest.TestSuite(
            [a_new_board, block_dropped, block_reaches_bottom,
            block_lands_on_another])

    def new_board_suite(self):
        return self.loader.loadTestsFromTestCase(ANewBoard)

    def when_a_block_is_dropped_suite(self):
        return self.loader.loadTestsFromTestCase(WhenABlockIsDropped)

    def when_a_block_reaches_the_bottom_suite(self):
        return self.loader.loadTestsFromTestCase(WhenABlockReachesTheBottom)

    def block_lands_on_another(self):
        return self.loader.loadTestsFromTestCase(WhenABlockLandsOnAnotherBlock)

class ANewBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(3, 3)

    def test_is_empty(self):
        expected_board = 3 * "...\n"
        self.assertEqual(expected_board, str(self.board))

    def test_has_no_falling_blocks(self):
        self.assertFalse(self.board.has_falling_pieces())

    def test_cannot_tick(self):
        with self.assertRaises(IllegalStateException):
            self.board.tick()

class WhenABlockIsDropped(unittest.TestCase):
    def setUp(self):
        self.board = Board(3, 3)
        self.board.drop(Piece('X'))

    def test_a_block_is_falling(self):
        self.assertTrue(self.board.has_falling_pieces())

    def test_block_starts_from_the_top_middle(self):
        expected_board = ".X.\n" + 2 * "...\n"
        self.assertEqual(expected_board, str(self.board))

    def test_block_moves_down_one_row_per_tick(self):
        self.board.tick()
        expected_board = "...\n" + ".X.\n" + "...\n"
        self.assertEqual(expected_board, str(self.board))

    def test_at_most_one_block_may_be_falling_at_a_time(self):
        with self.assertRaises(IllegalStateException):
            self.board.drop(Piece('Y'))
        expected_board = ".X.\n" + 2 * "...\n"
        self.assertEqual(expected_board, str(self.board))

class WhenABlockReachesTheBottom(unittest.TestCase):
    def setUp(self):
        self.board = Board(3, 3)
        self.board.drop(Piece('X'))
        self.board.tick()
        self.board.tick()

    def test_block_is_still_falling_on_the_last_row(self):
        self.assertTrue(self.board.has_falling_pieces())
        expected_board = 2 * "...\n" + ".X.\n"
        self.assertEqual(expected_board, str(self.board))

    def test_block_stops_when_it_hits_the_bottom(self):
        self.board.tick()
        self.assertFalse(self.board.has_falling_pieces())
        expected_board = 2 * "...\n" + ".X.\n"
        self.assertEqual(expected_board, str(self.board))
        with self.assertRaises(IllegalStateException):
            self.board.tick()

class WhenABlockLandsOnAnotherBlock(unittest.TestCase):
    def setUp(self):
        self.board = Board(3, 3)
        self.board.drop(Piece('X'))
        self.board.tick()
        self.board.tick()
        self.board.tick()
        self.board.drop(Piece('Y'))
        self.board.tick()
        self.expected_board = "...\n" + ".Y.\n" + ".X.\n"

    def test_block_is_still_falling_right_above_the_other_block(self):
        self.assertTrue(self.board.has_falling_pieces())
        self.assertEqual(self.expected_board, str(self.board))

    def test_block_stops_when_it_hits_another_block(self):
        self.board.tick()
        self.assertFalse(self.board.has_falling_pieces())
        self.assertEqual(self.expected_board, str(self.board))
        with self.assertRaises(IllegalStateException):
            self.board.tick()

if __name__ == '__main__':
    unittest.main()
