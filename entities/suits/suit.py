class Suit:

    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return f"{self.symbol}"
