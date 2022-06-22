import numpy as np

def generate_dictionary(exactness):
    """
    Pair extrema of chebyshev polynomials with a Smolyak index

    Parameters
    ----------
    exactness : int
        the level of exactness

    Returns
    -------
    extrema_dict : dictionary
        2**(exactness)+1 extremuns with matching Smolyak index
    """

    m = 2**(exactness)+1

    if exactness == 0:
        extrema_dict = {}
        extrema_dict.update({1:0})
        return extrema_dict
    else:
        extrema_dict = generate_dictionary(exactness-1)
        for i in range(1,m+1):
            temp = round(-np.cos(np.pi*(i-1)/(m-1)),15) + 0
            if temp not in extrema_dict.values():
                extrema_dict.update({len(extrema_dict):temp})
        return extrema_dict
