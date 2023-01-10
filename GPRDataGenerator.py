import gprMax
from abc import abstractmethod

class Generator:
    def __init__(self, model, frequency, amplitude, phase, x, y, z):
        self.model = model
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase
        self.x = x
        self.y = y
        self.z = z
        self.batchSize = 512

    @abstractmethod
    def process(self):
        pass

    def generate(self):
        yield data
