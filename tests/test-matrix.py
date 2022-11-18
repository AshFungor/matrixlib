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

    # test single element notation
    def test_get_index(self):
        sample_matrix = Matrix([[1, 2, 3], [1, 2, 3]])
        self.assertEqual(sample_matrix[1][1], 1.)

    # test if IndexError raises when using single element notation
    def test_index_out_of_range(self):
        with self.assertRaises(IndexError):
            Matrix([[1, 2], [1, 2]])[1][3]

    # test column return
    def test_slice_get_column(self):
        sample_matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(sample_matrix[:][1], [[1], [4]])

    # get minor
    # (1 2 3)    (1 2)
    # (4 5 6) -> (4 5)
    # (7 8 9)
    def test_slice_get_minor(self):
        sample_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(sample_matrix[1:2][1:2], [[1, 2], [4, 5]])

    # test if copying matrix with [:][:] slices is possible
    def test_slice_get_entire_matrix(self):
        _l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        sample_matrix = Matrix(_l)
        self.assertEqual(sample_matrix[:][:], _l)

    # test row return
    def test_slice_get_row(self):
        sample_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(sample_matrix[1][:], [[1, 2, 3]])

    # test if step in slices works
    def test_slice_with_iterator(self):
        sample_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(sample_matrix[::2][::2], [[1, 3], [7, 9]])


if __name__ == "__main__":
    unittest.main()
