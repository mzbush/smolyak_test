import numpy as np
from .IndexGrid import IndexGrid
import basis_funs


class SurrogateFun():
    """Defines the surrogate function
    more explanation

    Attributes
    ----------
    index_grid : class IndexGrid
        the Smolyak grid

    basis_fun : class BasisFun
        the basis function

    range_dimension : list
        the ranges of the dimensions
    """

    def __init__(self, basis_fun, dimension, exactness, range_dimension):
        """Initializer
        """
        self.basis_fun = basis_fun
        index_per_level = selfbasis_fun.index_per_level()
        self.index_grid = IndexGrid(dimension,exactness,index_per_level)

        # make sure the range_dimension is the right size
        if len(range_dimension) != 2 or len(range_dimension[0]) != dimension:
            raise ValueError("Range should match number of dimensions")
        else:
            self.range_dimension = range_dimension

    def generate_coefficients(self):
        pass


    def generate_gridpoints(self):
        pass

    def surrogate_function(self,x):
        pass


