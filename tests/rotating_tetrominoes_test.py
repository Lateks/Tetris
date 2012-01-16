import unittest

class RotatingTetrominoesTestSuiteGenerator:
    def __init__(self):
        self.loader = unittest.TestLoader()

    def suite(self):
        all_shape_instances = self.all_shape_instances_suite()

    def all_shape_instances_suite(self):
        return self.loader.loadTestsFromTestCase(AllShapeInstances)

class AllShapeInstances(unittest.TestCase):
    def setUp(self):
        self.shape = Tetrominoe.T_SHAPE

    def test_are_immutable():
        original = str(self.shape)
        self.shape.rotate_right()
        self.assertEqual(original, str(self.shape))
        self.shape.rotate_left()
        self.assertEqual(original, str(self.shape))
