from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self) -> None: ...


class Eatable(ABC):
    @abstractmethod
    def eat(self) -> None: ...
