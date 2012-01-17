import unittest
import src.tetrominoe as tetrominoe

class RotatingTetrominoesTestSuiteGenerator:
    def __init__(self):
        self.loader = unittest.TestLoader()

    def suite(self):
        all_shape_instances = self.all_shape_instances_suite()
        t_shape = self.t_shape_suite()
        l_shape = self.l_shape_suite()
        j_shape = self.j_shape_suite()
        z_shape = self.z_shape_suite()
        s_shape = self.s_shape_suite()
        return unittest.TestSuite([all_shape_instances,
                                t_shape, l_shape, j_shape,
                                z_shape, s_shape])

    def all_shape_instances_suite(self):
        return self.loader.loadTestsFromTestCase(AllShapeInstances)

    def t_shape_suite(self):
        return self.loader.loadTestsFromTestCase(T_Shape)

    def l_shape_suite(self):
        return self.loader.loadTestsFromTestCase(L_Shape)

    def j_shape_suite(self):
        return self.loader.loadTestsFromTestCase(J_Shape)

    def z_shape_suite(self):
        return self.loader.loadTestsFromTestCase(Z_Shape)

    def s_shape_suite(self):
        return self.loader.loadTestsFromTestCase(S_Shape)

class AllShapeInstances(unittest.TestCase):
    def setUp(self):
        self.shape = tetrominoe.T_SHAPE

    def test_are_immutable(self):
        original = str(self.shape)
        self.shape.rotate_right()
        self.assertEqual(original, str(self.shape))
        self.shape.rotate_left()
        self.assertEqual(original, str(self.shape))

class T_Shape(unittest.TestCase):
    def setUp(self):
        self.shape = tetrominoe.T_SHAPE

    def test_is_shaped_like_T(self):
        expected_shape = ".T.\n" + \
                         "TTT\n" + \
                         "...\n"
        self.assertEqual(expected_shape, str(self.shape))

    def test_can_be_rotated_right_3_times(self):
        rotated_once   = ".T.\n" + \
                         ".TT\n" + \
                         ".T.\n"
        rotated_twice  = "...\n" + \
                         "TTT\n" + \
                         ".T.\n"
        rotated_thrice = ".T.\n" + \
                         "TT.\n" + \
                         ".T.\n"
        shape = self.shape.rotate_right()
        self.assertEqual(rotated_once, str(shape))
        shape = shape.rotate_right()
        self.assertEqual(rotated_twice, str(shape))
        shape = shape.rotate_right()
        self.assertEqual(rotated_thrice, str(shape))

    def test_can_be_rotated_left_3_times(self):
        rotated_once   = ".T.\n" + \
                         "TT.\n" + \
                         ".T.\n"
        rotated_twice  = "...\n" + \
                         "TTT\n" + \
                         ".T.\n"
        rotated_thrice = ".T.\n" + \
                         ".TT\n" + \
                         ".T.\n"
        shape = self.shape.rotate_left()
        self.assertEqual(rotated_once, str(shape))
        shape = shape.rotate_left()
        self.assertEqual(rotated_twice, str(shape))
        shape = shape.rotate_left()
        self.assertEqual(rotated_thrice, str(shape))

    def test_rotating_it_4_times_will_go_back_to_the_original_shape(self):
        original_shape = str(self.shape)
        shape = self.shape.rotate_right().rotate_right().rotate_right().rotate_right()
        self.assertEqual(original_shape, str(shape))
        shape = self.shape.rotate_left().rotate_left().rotate_left().rotate_left()
        self.assertEqual(original_shape, str(shape))

#class I_Shape(unittest.TestCase):
#    def setUp(self):
#        self.shape = tetrominoe.I_SHAPE
#
#    def test_is_shaped_like_I(self):
#        expected_shape = ".....\n" + \
#                         ".....\n" + \
#                         "IIII.\n" + \
#                         ".....\n" + \
#                         ".....\n"
#        self.assertEqual(expected_shape, str(self.shape))
#
#    def test_can_be_rotated_right_once(self):
#        expected_shape = ".....\n" + \
#                         "..I..\n" + \
#                         "..I..\n" + \
#                         "..I..\n" + \
#                         "..I..\n"
#        shape = self.shape.rotate_right()
#        self.assertEqual(expected_shape, str(shape))
#
#    def test_can_be_rotated_left_once(self):
#        expected_shape = ".....\n" + \
#                         "..I..\n" + \
#                         "..I..\n" + \
#                         "..I..\n" + \
#                         "..I..\n"
#        shape = self.shape.rotate_left()
#        self.assertEqual(expected_shape, str(shape))
#
#    def test_rotating_twice_will_get_back_to_the_original_shape(self):
#        original_shape = str(self.shape)
#        shape = self.shape.rotate_right().rotate_right()
#        self.assertEqual(original_shape, str(shape))
#        shape = shape.rotate_left().rotate_left()
#        self.assertEqual(original_shape, str(shape))
#
#class O_Shape(unittest.TestCase):
#    def setUp(self):
#        self.shape = tetrominoe.O_SHAPE
#        self.expected_shape = ".OO\n" + \
#                              ".OO\n" + \
#                              "...\n"
#
#    def test_is_shaped_like_O(self):
#        self.assertEqual(self.expected_shape, str(self.shape))
#
#    def test_can_not_be_rotated_right(self):
#        shape = self.shape.rotate_right()
#        self.assertEqual(self.expected_shape, str(shape))
#
#    def test_can_not_be_rotated_left(self):
#        shape = self.shape.rotate_left()
#        self.assertEqual(self.expected_shape, str(shape))

class L_Shape(unittest.TestCase):
    def setUp(self):
        self.shape = tetrominoe.L_SHAPE

    def test_is_shaped_like_L(self):
        expected_shape = "...\n" + \
                         "LLL\n" + \
                         "L..\n"
        self.assertEqual(expected_shape, str(self.shape))

    def test_can_be_rotated_right_3_times(self):
        rotated_once   = "LL.\n" + \
                         ".L.\n" + \
                         ".L.\n"
        rotated_twice  = "..L\n" + \
                         "LLL\n" + \
                         "...\n"
        rotated_thrice = ".L.\n" + \
                         ".L.\n" + \
                         ".LL\n"
        shape = self.shape.rotate_right()
        self.assertEqual(rotated_once, str(shape))
        shape = shape.rotate_right()
        self.assertEqual(rotated_twice, str(shape))
        shape = shape.rotate_right()
        self.assertEqual(rotated_thrice, str(shape))

    def test_can_be_rotated_left_3_times(self):
        rotated_once   = ".L.\n" + \
                         ".L.\n" + \
                         ".LL\n"
        rotated_twice  = "..L\n" + \
                         "LLL\n" + \
                         "...\n"
        rotated_thrice = "LL.\n" + \
                         ".L.\n" + \
                         ".L.\n"
        shape = self.shape.rotate_left()
        self.assertEqual(rotated_once, str(shape))
        shape = shape.rotate_left()
        self.assertEqual(rotated_twice, str(shape))
        shape = shape.rotate_left()
        self.assertEqual(rotated_thrice, str(shape))

    def test_rotating_it_4_times_will_go_back_to_the_original_shape(self):
        original_shape = str(self.shape)
        shape = self.shape.rotate_right().rotate_right().rotate_right().rotate_right()
        self.assertEqual(original_shape, str(shape))
        shape = self.shape.rotate_left().rotate_left().rotate_left().rotate_left()
        self.assertEqual(original_shape, str(shape))

class J_Shape(unittest.TestCase):
    def setUp(self):
        self.shape = tetrominoe.J_SHAPE

    def test_is_shaped_like_J(self):
        expected_shape = "...\n" + \
                         "JJJ\n" + \
                         "..J\n"
        self.assertEqual(expected_shape, str(self.shape))

    def test_can_be_rotated_right_3_times(self):
        rotated_once   = ".J.\n" + \
                         ".J.\n" + \
                         "JJ.\n"
        rotated_twice  = "J..\n" + \
                         "JJJ\n" + \
                         "...\n"
        rotated_thrice = ".JJ\n" + \
                         ".J.\n" + \
                         ".J.\n"
        shape = self.shape.rotate_right()
        self.assertEqual(rotated_once, str(shape))
        shape = shape.rotate_right()
        self.assertEqual(rotated_twice, str(shape))
        shape = shape.rotate_right()
        self.assertEqual(rotated_thrice, str(shape))

    def test_can_be_rotated_left_3_times(self):
        rotated_once   = ".JJ\n" + \
                         ".J.\n" + \
                         ".J.\n"
        rotated_twice  = "J..\n" + \
                         "JJJ\n" + \
                         "...\n"
        rotated_thrice = ".J.\n" + \
                         ".J.\n" + \
                         "JJ.\n"
        shape = self.shape.rotate_left()
        self.assertEqual(rotated_once, str(shape))
        shape = shape.rotate_left()
        self.assertEqual(rotated_twice, str(shape))
        shape = shape.rotate_left()
        self.assertEqual(rotated_thrice, str(shape))

    def test_rotating_it_4_times_will_go_back_to_the_original_shape(self):
        original_shape = str(self.shape)
        shape = self.shape.rotate_right().rotate_right().rotate_right().rotate_right()
        self.assertEqual(original_shape, str(shape))
        shape = self.shape.rotate_left().rotate_left().rotate_left().rotate_left()
        self.assertEqual(original_shape, str(shape))

class Z_Shape(unittest.TestCase):
    def setUp(self):
        self.shape = tetrominoe.Z_SHAPE

    def test_is_shaped_like_Z(self):
        expected_shape = "...\n" + \
                         "ZZ.\n" + \
                         ".ZZ\n"
        self.assertEqual(expected_shape, str(self.shape))

    def test_can_be_rotated_right_once(self):
        expected_shape = ".Z.\n" + \
                         "ZZ.\n" + \
                         "Z..\n"
        shape = self.shape.rotate_right()
        self.assertEqual(expected_shape, str(shape))

    def test_can_be_rotated_left_once(self):
        expected_shape = "..Z\n" + \
                         ".ZZ\n" + \
                         ".Z.\n"
        shape = self.shape.rotate_left()
        self.assertEqual(expected_shape, str(shape))

#    def test_rotating_twice_will_get_back_to_the_original_shape(self):
#        original_shape = str(self.shape)
#        shape = self.shape.rotate_right().rotate_right()
#        self.assertEqual(original_shape, str(shape))
#        shape = self.shape.rotate_left().rotate_left()
#        self.assertEqual(original_shape, str(shape))

class S_Shape(unittest.TestCase):
    def setUp(self):
        self.shape = tetrominoe.S_SHAPE

    def test_is_shaped_like_S(self):
        expected_shape = "...\n" + \
                         ".SS\n" + \
                         "SS.\n"
        self.assertEqual(expected_shape, str(self.shape))

    def test_can_be_rotated_right_once(self):
        expected_shape = "S..\n" + \
                         "SS.\n" + \
                         ".S.\n"
        shape = self.shape.rotate_right()
        self.assertEqual(expected_shape, str(shape))

    def test_can_be_rotated_left_once(self):
        expected_shape = ".S.\n" + \
                         ".SS\n" + \
                         "..S\n"
        shape = self.shape.rotate_left()
        self.assertEqual(expected_shape, str(shape))

#    def test_rotating_twice_will_get_back_to_the_original_shape(self):
#        original_shape = str(self.shape)
#        shape = self.shape.rotate_right().rotate_right()
#        self.assertEqual(original_shape, str(shape))
#        shape = self.shape.rotate_left().rotate_left()
#        self.assertEqual(original_shape, str(shape))
