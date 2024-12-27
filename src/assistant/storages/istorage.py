from abc import ABC, abstractmethod

class IStorage(ABC):
    alias = None
    @abstractmethod
    def set(self, key:str, value):
        pass

    @abstractmethod
    def get(self, key:str):
        pass

    @abstractmethod
    def exists(self, key:str) -> bool:
        pass

    @abstractmethod
    def delete(self, key:str):
        pass