# Builder Model

from GPRDataBuilder import GPRDataBuilder
from NormalGPRDataBuilder import NormalGPRDataBuilder


class Director:

    def __init__(self):
        self.builder = NormalGPRDataBuilder

    def runSimulator(self):
        self.builder.AScan()


if __name__ == "__main__":
    director = Director()
    director.runSimulator()
