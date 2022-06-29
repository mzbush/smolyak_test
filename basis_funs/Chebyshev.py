import numpy as np


class Chebyshev(BasisFun):
    """Generate basis function
    Describes the basis function used to construct the surrogate function
    creates a dictionary of extrema to correspond to the Smolyak indices

    Attributes
    ----------
    """

    def generate_dictionary(exactness):
        """Pair Smolyak index with extrema
        Generate dictionary of chebyshev polynomial extrema that
        correspond to a Smolyak index and a list of the number of 
        extrema in each grid level

        Parameters
        ----------
        exactness : int
            the level of exactness

        Returns
        -------
        extrema_dict : dictionary
            2**(exactness)+1 extrema with matching Smolyak index
        
        index_per_level : list
            number of indices for each grid level
        """

        m = 2**(exactness)+1
        if exactness == 0:
            extrema_dict = {}
            extrema_dict.update({1:0})
            index_per_level = [1]
        else:
            extrema_dict,index_per_level = generate_dictionary(exactness-1)
            counter_index = 0
            for i in range(1,m+1):
                extremum = round(-np.cos(np.pi*(i-1)/(m-1)),15) + 0
                if extremum not in extrema_dict.values():
                    extrema_dict.update({len(extrema_dict):extremum})
                    counter_index += 1
            index_per_level.append(counter_index)
        return extrema_dict,index_per_level

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

