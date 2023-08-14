from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        print('hi')
        pass
class Laptop(Computer):
    def process(self):
        print('hello')


lap = Laptop()
lap.process()