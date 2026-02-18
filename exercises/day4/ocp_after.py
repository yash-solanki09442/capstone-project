from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float: ...


class RegularDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount * 0.95


class PremiumDiscount(DiscountStrategy):
    def apply(self, amount: float) -> float:
        return amount * 0.90


def calculate_discount(strategy: DiscountStrategy, amount: float) -> float:
    return strategy.apply(amount)
