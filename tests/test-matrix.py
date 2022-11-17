import unittest
from matrixlib.matrix import Matrix

class TestMatrixClass(unittest.TestCase):

    def setUp(self):
        self.sample_matrix = Matrix([[1, 2, 3], [1, 2, 3]])

    def test_simple_dimensions(self):
        self.assertEqual(self.sample_matrix.get_dimensions(), (2, 3))