import numpy as np
from .BasisFun import BasisFun

class Chebyshev(BasisFun):
    """Chebyshev polynomial of the first kind basis function

    Attributes
    ----------
    exactness : int
        level of exactness
    """

    def __init__():
        pass

    def generate_dictionary(exactness):
        """Generates extrema dictionary
        Pair extrema of chebyshev polynomial with a Smolyak index and 
        generate the index per grid level for the basis function

        Parameters
        ----------
        exactness : int
            level of exactness

        Returns
        -------
        extrema_dict : dictionary
            2**(exactness)+1 extrema with matching Smolyak index

        index_per_level : list
            number of indexes for each grid level
        """
        m = 2**(exactness)+1

        if exactness == 0:
            extrema_dict = {}
            extrema_dict.update({1:0})
            index_per_level = [1]
        else:
            extrema_dict,index_per_level = generate_dictionary(exactness-1)
            counter_index = 0
            for i in range(1+m+1):
                extremum = round(-np.cos(np.pi*(i-1)/(m-1)),15) + 0
                if extremum not in extrema_dict.values();
                extrema_dict,update({len(extrema_dict):temp})
                counter_index += 1
            index_per_level.append(counter_index)
        return extrema_dict,index_per_level

    def basis_fun(x,n):
        """Terms of basis function
        Returns the output of an nth degree chebyshev polynomial of the
        1st kind with input x

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
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            k_lim = floor(n/2)
            answer = 0
            for k in range(0,k_lim+1):
                answer += comb(n,2*k)*((x**2 - 1)**k)*(x**(n-2*k))
            return answer
