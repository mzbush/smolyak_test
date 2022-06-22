from abc import ABC, abstractmethod

class BasisFun(ABC):
    

    @abstractmethod
    def generate_dictionary(exactness):
        pass

    @abstractmethod
    def basis_fun(x,n):
        """terms of basis function
        returns the output of an nth degree basis function with input x

        Parameters
        ----------
        x : float
            input

        n : int
            degree

        Returns
        -------
        y : float
            output
        """
        pass
