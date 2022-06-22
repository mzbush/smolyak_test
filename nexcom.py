def nexcom(n,k):
    """
    Creates list of all combinations of integers with the same length
    and sum

    Parameters
    ----------
    n : int
        sum
    k ; int
        length of each combination

    Returns
    -------
    r : list
        list of combinations
    """
    r_initial = np.zeros(k,dtype=int)
    r_initial[0] = n
    r = [list(r_initial)]
    t = n
    h = -1
    if (k == 1) or n == 0:
        return r
    mtc = True
    r_temp = r[0].copy()
    while mtc:
        if t > 1:
            h = -1
        h = h+1
        t = r_temp[h]
        r_temp[h] = 0
        r_temp[0] = t-1
        r_temp[h+1] = r_temp[h+1]+1
        r.append(r_temp.copy())
        mtc = r_temp[k-1] != n
    return r

def nexcom_min_1(n,k):
    """
    Creates list of all combinations of integers with the same length
    and sum where the minimum of each individual number is 1

    Parameters
    ----------
    n : int
        sum
    k : int
        length of each combination

    Returns
    -------
    r : list
        length of each combination

    Raises
    ------
    Value Error
        if the sum is greater than or equal to the length of combinations
    """
    if n < k:
        raise ValueError("sum must be >= length")
    return [[x+1 for x in combin] for combin in nexcom(n-k,k)]
