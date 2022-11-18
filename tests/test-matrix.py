import unittest
from matrixlib.matrix import Matrix


class TestMatrixClass(unittest.TestCase):

    # N1 test if constructor breaks if size of rows is different:
    # (1 2)
    # (1 2 3 4)
    # - unacceptable
    def test_diff_row_size_constructor(self):
        with self.assertRaises(ValueError):
            Matrix([[1, 2], [1, 2, 3, 4]])

    # N2 test if this function works as expected
    def test_simple_dimensions(self):
        sample_matrix = Matrix([[1, 2, 3], [1, 2, 3]])
        self.assertEqual(sample_matrix.get_dimensions(), (2, 3))

    # N3 test single element notation
    def test_get_index(self):
        sample_matrix = Matrix([[1, 2, 3], [1, 2, 3]])
        self.assertEqual(sample_matrix[1][1], 1.)

    # N4 test if IndexError raises when using single element notation
    def test_index_out_of_range(self):
        with self.assertRaises(IndexError):
            Matrix([[1, 2], [1, 2]])[1][3]

    # N5 test column return
    def test_slice_get_column(self):
        sample_matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(sample_matrix[:][1], [[1], [4]])

    # N6 get minor
    # (1 2 3)    (1 2)
    # (4 5 6) -> (4 5)
    # (7 8 9)
    def test_slice_get_minor(self):
        sample_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(sample_matrix[1:2][1:2], [[1, 2], [4, 5]])

    # N7 test if copying matrix with [:][:] slices is possible
    def test_slice_get_entire_matrix(self):
        _l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sample_matrix = Matrix(_l)
        self.assertEqual(sample_matrix[:][:], _l)

    # N8 test row return
    def test_slice_get_row(self):
        sample_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(sample_matrix[1][:], [[1, 2, 3]])

    # N9 test if step in slices works
    def test_slice_with_iterator(self):
        sample_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(sample_matrix[::2][::2], [[1, 3], [7, 9]])

    # N10 test if '+' operator works
    def test_add_operator(self):
        _1 = Matrix([[1, 2], [3, 4]])
        _2 = Matrix([[1, 2], [3, 4]])
        self.assertEqual((_1 + _2)[:][:], [[2, 4], [6, 8]])

    # N11 test if matrixes with different sizes could not be added to
    # each other
    def test_add_diff_dimensions_error(self):
        with self.assertRaises(ValueError):
            _1 = Matrix([[1, 2, 1], [3, 4, 4]])
            _2 = Matrix([[1, 2], [3, 4]])
            _1 + _2

    # test if matrix can only be added to matrix
    def test_add_diff_type_error(self):
        with self.assertRaises(ValueError):
            _1 = Matrix([[1, 2, 1], [3, 4, 4]])
            _2 = 2
            _1 + _2


if __name__ == "__main__":
    unittest.main()
