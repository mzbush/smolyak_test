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
