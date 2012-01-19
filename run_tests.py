import unittest
from tests.falling_blocks_test import FallingBlockTestSuiteGenerator
from tests.rotating_pieces_of_blocks_test import RotatingPiecesOfBlocksTestSuiteGenerator
from tests.rotating_tetrominoes_test import RotatingTetrominoesTestSuiteGenerator
from tests.falling_pieces_test import FallingPiecesTestSuiteGenerator

def run_tests():
    falling_blocks_suite = get_falling_blocks_suite()
    rotating_pieces_suite = get_rotating_pieces_suite()
    rotating_tetrominoes_suite = get_rotating_tetrominoes_suite()
    falling_pieces_suite = get_falling_pieces_suite()

    test_suite = unittest.TestSuite([falling_blocks_suite,
        rotating_pieces_suite, rotating_tetrominoes_suite,
        falling_pieces_suite])
    unittest.TextTestRunner(verbosity = 2).run(test_suite)

def get_falling_blocks_suite():
    test_suite_gen = FallingBlockTestSuiteGenerator()
    return test_suite_gen.suite()

def get_rotating_pieces_suite():
    test_suite_gen = RotatingPiecesOfBlocksTestSuiteGenerator()
    return test_suite_gen.suite()

def get_rotating_tetrominoes_suite():
    test_suite_gen = RotatingTetrominoesTestSuiteGenerator()
    return test_suite_gen.suite()

def get_falling_pieces_suite():
    test_suite_gen = FallingPiecesTestSuiteGenerator()
    return test_suite_gen.suite()

if __name__ == '__main__':
    run_tests()
