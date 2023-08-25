# Builder Model

from NormalGPRDataBuilder import NormalGPRDataBuilder


class Director:

    def __init__(self):
        self.builder = NormalGPRDataBuilder()

    def runSimulator(self):
        self.builder.AScan()


if __name__ == "__main__":
    director = Director()
    # Batch generate A-Scan
    director.runSimulator()

    # Batch generate B-Scan

