from typing import TypeVar, Iterable

class Matrix():

    def __init__(self, matrix_iterable: Iterable[Iterable[float]]):

        matrix_list = []
        for row in matrix_iterable:
            matrix_list.append(list(row))
        
        self.matrix = matrix_list

    def get_dimensions(self) -> (int, int):

        rows = len(self.matrix)
        columns = len(self.matrix[0])

        return (rows, columns)


            
        
