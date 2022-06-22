from nexcom import nexcom, nexcom_min_1
from itertools import product,accumulate

class IndexGrid()
    __init__(dimension, exactness, index_per_level):
        self.dimension = dimension
        self.exactness = exactness
        self.index_per_level = index_per_level

    @property
    def dimension(self):
        return self.dimension

    @property
    def exactness(self):
        return self.exactness

    @property
    def index_per_level(self):
        return self.index_per_level

    @dimension.setter
    def dimension(self, d)
        self.dimension = d

    @exactness.setter
    def exactness(self, e)
        self.exactness = e

    @index_per_level.setter
    def index_per_level(self, ipl)
        self.index_per_level = ipl

    def grid_levels(self):
        """
        Computes grid levels

        Returns
        -------
        grid_levels : list
            n-dimensional vector of valid combinations of grid levels
        """
        max_level = 1 + self.exactness
        grid_levels = []
        for i in range(self.dimension,self.dimension+self.exactness+1):
            grid_levels.extend(nexcom_min_1(i,n))
        return grid_levels

    def Smolyak_indices(self):
        """
        Creates Smolyak indices

        Returns
        -------
        Smolyak_indices : list of truples
            Smolyak indices where each number is associated with a term
            of the surrogate function and an extrema of the surrogate
            function
        """
        grid_level = grid_levels()
        Smolyak_indices = []
        combin_list = grid_level
        cummul_index_per_level = [0]
        cummul_index_per_level.extend([x := x + i for i in a])
        for i in range(0,len(grid_level)):
            for j in range(0,n):
                num_in_lev = self.index_per_level[grid_level[i][j]-1]
                num_bef_lev = cummul_index_per_level[grid_level[i][j]-1]
                combin_list = list(range(num_before_lev, num_in_lev+num_before_lev))
            combin_all = list(product(*combin_list[i]))
            Smolyak_indices += combin_all
        return Smolyak_indices

