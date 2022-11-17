from typing import TypeVar, Iterable

T = TypeVar('T', int, float)


class Matrix():
    """
    This class is used to represent matrixes
    and perform specific actions with them.

    Methods
    ----------
    get_dimensions(self) -> (int, int)
        use this method to get dimensions of
        the matrix, in the following form
        (number_of_rows, number_of_columns)
    display(self, precision: int) -> None
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
