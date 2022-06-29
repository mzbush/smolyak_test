import numpy as np
from basis_funs.BasisFun import BasisFun
from .IndexGrid import IndexGrid

class SurrogateFun():
    """Surrogate Function of data
    Put description here

    Attributes
    ----------
    index_grid : class IndexGrid
        points on grid as Smolyak indices

    basis_fun : abstract class BasisFun
        basis function

    extrema_dict : dictionary
        dictionary for extrema to Smolyak index

    TBD : TBD
        something related to output of real function?
    """
    def __init__(self, basis_fun, dimension, exactness):
        """Initializer
        longer description here

        Parameters
        ----------
        basis_fun : BasisFun class
            basis function

        dimension : int
            number of variables the surrogate function must account for

        exactness : int
            the level of exactness
        """
        self.basis_fun = basis_fun
        self.extrema_dict,ipl = self.basis_fun.generate_dictionary(exactness)
        self.index_grid(dimension,exactness,ipl)

    def create_gridpoints(self):
        pass

    def create_coeff(self):
        pass

