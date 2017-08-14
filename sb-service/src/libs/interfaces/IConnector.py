from abc import ABC, abstractmethod


class IConnector(ABC):

    @abstractmethod
    def connect(self, args):
        pass
