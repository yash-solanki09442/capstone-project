from dataclasses import dataclass
from typing import Protocol


class Shape(Protocol):
    def area(self) -> int: ...


@dataclass(frozen=True)
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height


@dataclass(frozen=True)
class Square:
    size: int

    def area(self) -> int:
        return self.size * self.size
