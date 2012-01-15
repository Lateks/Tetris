import unittest
from tests.falling_blocks_test import FallingBlockTestSuiteGenerator

def run_tests():
    test_suite_gen = FallingBlockTestSuiteGenerator()
    test_suite = test_suite_gen.suite()
    unittest.TextTestRunner(verbosity = 2).run(test_suite)

if __name__ == '__main__':
    run_tests()
