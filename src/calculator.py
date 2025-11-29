class Calculator:
    """Prosty kalkulator z podstawowymi operacjami."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Nie można dzielić przez zero.")
        return a / b


def safe_divide(a: float, b: float) -> float | None:
    """Dzieli bez wyjątku — jeśli b=0, zwraca None."""
    if b == 0:
        return None
    return a / b


if __name__ == "__main__":
    calc = Calculator()
    print("3 + 5 =", calc.add(3, 5))
    print("10 / 2 =", calc.divide(10, 2))
