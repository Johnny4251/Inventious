from abc import ABC, abstractmethod

class State(ABC):
    
    @abstractmethod
    def render(self, state):
        pass