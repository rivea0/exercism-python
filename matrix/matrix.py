class Matrix:
    def __init__(self, matrix_string):
        self.s = matrix_string


    def row(self, index):
        """Return a list of rows, left-to-right top-to-bottom."""
        groups = [i for i in self.s.split('\n')]
        rws = [int(i) for i in groups[index-1].split(' ')]
        return rws


    def column(self, index):
        """Return a list of columns, top-to-bottom left-to-right."""
        groups = [i.split(' ') for i in self.s.split('\n')]
        cols = [int(i[index-1]) for i in groups]
        return cols
