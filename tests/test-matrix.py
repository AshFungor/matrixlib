import unittest
from matrixlib.matrix import Matrix


class TestMatrixClass(unittest.TestCase):

    # test if constructor breaks if size of rows is different:
    # (1 2)
    # (1 2 3 4)
    # - unacceptable
    def test_diff_row_size_constructor(self):
        with self.assertRaises(ValueError):
            Matrix([[1, 2], [1, 2, 3, 4]])

    # test if this function works as expected
    def test_simple_dimensions(self):
        sample_matrix = Matrix([[1, 2, 3], [1, 2, 3]])
        self.assertEqual(sample_matrix.get_dimensions(), (2, 3))
