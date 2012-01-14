import unittest
from tests.falling_blocks_test import FallingBlockTestSuites

def run_tests():
    testsuite = FallingBlockTestSuites.suite()
    unittest.TextTestRunner(verbosity = 2).run(testsuite)

if __name__ == '__main__':
    run_tests()
