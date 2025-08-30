class Rank:

    def __init__(self, name: str, symbol: str, value: int) -> None:
        self.name = name
        self.symbol = symbol
        self.value = value

    def __repr__(self):
        return f"{self.name}"
