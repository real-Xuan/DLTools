# from abc import abstractclassmethod
from GPRData import GPRData


# @abstractclassmethod
class GPRDataBuilder:

    def __init__(self):
        self.GPRData = GPRData()

    def AScan(self):
        pass

    def BScan(self):
        pass

    def CScan(self):
        pass

    def DScan(self):
        pass


class ConstructBuilder(GPRDataBuilder):
    def AScan(self):
        pass

    def BScan(self):
        pass

    def CScan(self):
        pass

    def DScan(self):
        pass
