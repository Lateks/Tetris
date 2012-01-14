import unittest
from src.board import Board

class FallingBlockTestSuites:
    @staticmethod
    def suite():
        a_new_board_tests = FallingBlockTestSuites.new_board_suite()
        return a_new_board_tests

    @staticmethod
    def new_board_suite():
        tests = ["test_is_empty"]
        return unittest.TestSuite(map(ANewBoard, tests))

class ANewBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(3, 3)

    def test_is_empty(self):
        expected_board = 3 * "...\n"
        self.assertEqual(expected_board, str(self.board))

    #def test_has_no_falling_blocks(self):
    #    self.assertFalse(board.has_falling())

#class WhenABlockIsDropped(unittest.TestCase):
#    def setUp(self):
#        self.board = Board(3, 3)
#        self.board.drop(Block('X'))

#    def test_a_block_is_falling(self):
#        self.assertTrue(self.board.has_falling())

#    def test_block_starts_from_the_top_middle(self)
#        expected_board = ".X.\n" + 2 * "...\n"
#        self.assertEqual(expected_board, str(self.board))

#    def test_block_moves_down_one_row_per_tick(self):
#        self.board.tick()
#        expected_board = "...\n" + ".X.\n" + "...\n"
#        self.assertEqual(expected_board, str(self.board))

#    def test_at_most_one_block_may_be_falling_at_a_time(self):
#        with self.assertRaises(IllegalStateException):
#            self.board.drop(Block('Y'))
#        expected_board = ".X.\n" + 2 * "...\n"
#        self.assertEqual(expected_board, str(self.board))

#class WhenABlockReachesTheBottom(unittest.TestCase):
#    def setUp(self):
#        self.board = Board(3, 3)
#        self.board.drop(new Block('X'))
#        self.board.tick()
#        self.board.tick()

#    def test_block_is_still_falling_on_the_last_row(self):
#        self.assertTrue(self.board.has_falling())
#        expected_board = 2 * "...\n" + ".X.\n"
#        self.assertEqual(expected_board, str(self.board)

#    def test_block_stops_when_it_hits_the_bottom(self):
#        self.board.tick()
#        assertFalse(self.board.has_falling())
#        expected_board = 2 * "...\n" + ".X.\n"
#        self.assertEqual(expected_board, str(self.board))

#class WhenABlockLandsOnAnotherBlock(unittest.TestCase):
#    def setUp(self):
#        self.board = Block(3, 3)
#        self.board.drop(Block('X'))
#        self.board.tick()
#        self.board.tick()
#        self.board.tick()
#        board.drop(Block('Y'))
#        board.tick()
#        self.expected_board = "...\n" + ".Y.\n" + ".X.\n"

#    def test_block_is_still_falling_right_above_the_other_block(self):
#        self.assertTrue(self.board.has_falling())
#        self.assertEqual(self.expected_board, str(self.board))

#    def test_block_stops_when_it_hits_another_block(self):
#        self.board.tick()
#        self.assertFalse(self.board.has_falling())
#        self.assertEqual(self.expected_board, str(self.board))

if __name__ == '__main__':
    unittest.main()
