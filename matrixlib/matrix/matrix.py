from typing import TypeVar, Iterable
from copy import deepcopy
from matrix_errors import DimensionsError

# type variables describe method's signature
T = TypeVar('T', int, float)
In = TypeVar('In', int, slice)
R = TypeVar('R', float, list[list[float]])
M = TypeVar('M', 'Matrix', float, int)


# purely helper class for using slice feature.
# the first slice returns this class with selected rows
# passed to constructor, second slice selects columns
class _TempMatrixSlice():

    def __init__(self, matrix_iterable: list[list[float]]):
        self.__matrix = matrix_iterable

    def __getitem__(self, request: In) -> R:
        result = []
        if isinstance(request, int):
            for row in self.__matrix:
                result.append([row[request - 1]])
        elif isinstance(request, slice):
            start = 1 if request.start is None else request.start
            for row in self.__matrix:
                result.append(
                    row[start - 1:request.stop:request.step])
        else:
            raise ValueError("parameter must be of type int or slice")

        if len(result) == 1 and len(result[0]) == 1:
            return result[0][0]
        else:
            return result


class Matrix():
    """
    This class is used to represent matrixes
    and perform specific actions with them.

    Methods
    ----------
    get_dimensions() -> (int, int)
        use this method to get dimensions of
        the matrix, in the following form
        (number_of_rows, number_of_columns)
    display(precision: int) -> None
        method is used to print matrix's
        contents to console
    """

    def __init__(self, matrix_iterable: list[list[T]]):
        """
        base class constructor. Note, elements of matrix are
        converted to float type after inner initialization.

        Parameters
        ----------
        matrix_iterable : list[list[T]]
            nested array of lists that represent matrix elements

        Raises
        ----------
        ValueError
            elements of nested lists must be T-type (int, float),
            also nested lists must be the same size
        TypeError
            nested iterables must be lists, uniting entity must
            be iterable at least
        """

        columns = None
        matrix_list = []

        for row in matrix_iterable:
            matrix_list.append(list())
            columns = len(row) if columns is None else columns
            if columns != len(row):
                raise ValueError("the size of rows must be the same")

            for element in row:
                if isinstance(element, float) or isinstance(element, int):
                    matrix_list[-1].append(float(element))
                else:
                    raise ValueError("elements of matrix must be float or int")

        self.__matrix = matrix_list

    def get_dimensions(self) -> (int, int):
        """
        method is used to determine matrix size

        Returns
        ----------
        (int, int)
            a tuple where the first element is a number
            of rows, second - columns
        """
        rows = len(self.__matrix)
        columns = len(self.__matrix[0])

        return (rows, columns)

    def display(self, precision: int) -> None:
        """
        method is used to print matrix's
        contents to console

        Parameters
        ----------
        precision: int
            states how many digits are printed
            in the fractional part of each element
        """
        # helper function, the only reason it exists is that
        # lambda couldn't manage to accommodate formatting
        def el_format(element, precision):
            cut_element = str(round(element, precision))

            return cut_element + '0' * \
                (precision - len(cut_element[cut_element.find('.'):]) + 1)

        for row in self.__matrix:
            print(' '.join(
                map(lambda element: el_format(element, precision), row)))

    def __getitem__(self, request: In) -> _TempMatrixSlice:
        """
        standard index access to matrix elements.
        Remember to always use double square brackets
        ([][]) when using this method.

        Parameters
        ----------
        request: TypeVar(int, slice)
            use [index] to get access to specific row
            or column, slices are also supported

        Raises
        ----------
        ValueError
            request must be int or slice type

        Returns
        ----------
        TypeVar(list[list[float]], float)
            returns single element if [x][y]
            notation is used, otherwise
            returns list[list[float]]
        """

        if isinstance(request, int):
            return _TempMatrixSlice([self.__matrix[request - 1]])
        if isinstance(request, slice):
            start = 1 if request.start is None else request.start
            return _TempMatrixSlice(
                self.__matrix[start - 1:request.stop:request.step])
        else:
            raise ValueError("parameter must be of type int or slice")

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """
        operator '+' support. Note, matrixes must
        be the same size.

        Parameters
        ----------
        other: Matrix
            second matrix to add to the first

        Raises
        ----------
        ValueError
            this error appears if you try to
            add differently sized matrix
            or non-matrix object

        Returns
        ----------
        Matrix
            Matrix which is the result
            of adding one to the other
        """
        if isinstance(other, Matrix):
            rows, columns = other.get_dimensions()
            if self.get_dimensions() == (rows, columns):
                other_raw_matrix = other[:][:]
                for row in range(rows):
                    for column in range(columns):
                        other_raw_matrix[row][column] += \
                            self[row + 1][column + 1]
                return Matrix(other_raw_matrix)
            else:
                raise ValueError("matrixes must be the same size")
        else:
            raise ValueError(
                f"operand \"+\" is not supported for Matrix and {type(other)}")

    def __mul__(self, other: M) -> 'Matrix':
        """
        multiplying method for either multiplying
        the matrix by a number or another matrix

        Parameters
        ----------
        other: TypeVar('Matrix', float, int)
            an instance to multiply by

        Raises
        ----------
        ValueError
            raised if parameter does not
            match any of types (int, float, Matrix)

        Returns
        ----------
        Matrix
            the result of multiplication

        """
        if isinstance(other, float) or isinstance(other, int):
            rows, columns = self.get_dimensions()
            new_matrix = deepcopy(self.__matrix)
            for row in range(rows):
                for column in range(columns):
                    new_matrix[row][column] *= other
            return Matrix(new_matrix)

        elif isinstance(other, Matrix):
            f_rows, f_columns = self.get_dimensions()
            s_rows, s_columns = other.get_dimensions()
            if f_rows != s_columns:
                raise ValueError("number of rows in first matrix must be equal\
                    to number of columns in other")
            size = min(f_rows, s_columns)
            new_matrix = [[0 for column in range(size)] for row in range(size)]

            def evaluate_el(row, column):
                result = 0
                for i in range(len(row)):
                    result += row[i] * column[i]
                return result

            for row in range(size):
                for column in range(size):
                    new_matrix[row][column] = \
                        evaluate_el(self[row + 1][:][0], list(
                            map(lambda el: el[0], other[:][column + 1])))

            return Matrix(new_matrix)

        else:
            raise ValueError(
                f"operand \"*\" is not supported for Matrix and {type(other)}")

    # methods to make life easier
    # no need to provide docs on them
    def __rmul__(self, other: M) -> 'Matrix':
        return self * other

    def __neg__(self) -> 'Matrix':
        return self * -1
