
from abc import ABC, abstractmethod
​
class State(ABC):
    def __call__(self, command):
        if command == 'state':
            return str(self)
        if command == 'stop':
            return 'accept' if self.is_final() else 'reject'
        else:
            return self.next_state(command)
​
    @abstractmethod
    def next_state(self, input):
        raise NotImplementedError
​
    def is_final(self):
        return False
    
    def __str__(self):
        return type(self).__name__
​
​
class S0(State):
    def next_state(self, input):
        return {
            0: self,
            1: S1(),
        }[input]
​
    def is_final(self):
        return True
​
​
class S1(State):
    def next_state(self, input):
        return {
            0: S2,
            1: S0,
        }[input]()
​
​
class S2(State):
    def next_state(self, input):
        return {
            0: S1(),
            1: self,
        }[input]
​
​
divisible = S0()

