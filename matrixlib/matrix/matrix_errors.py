
# base class for errors
class Error(Exception):
    """
    base class for matrix errors
    """


class DimensionsError(Error):
    """
    An error class which is intended to cover errors related to wrong
    matrixes' dimensions upon processing operations with them.

    Attributes 
    ----------
    a_dimensions: (int, int)
        dimensions of matrix A
    b_dimensions: (int, int)
        dimensions of matrix B
    msg: str
        custom message to be
        used before standard
        error string
    """
    def __init__(
            self, a_dimensions: (int, int),
            b_dimensions: (int, int), message='dimension error'):

        self.a_dimensions = a_dimensions
        self.b_dimensions = b_dimensions
        self.msg = message
        super().__init__(message)

    def __str__(self):
        return f'{self.msg}: \
            {self.a_dimensions} and {self.b_dimensions} are not matching'
