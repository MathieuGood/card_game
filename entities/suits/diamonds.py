from entities.suits.suit import Suit


class Diamonds(Suit):

    def __init__(self) -> None:
        super().__init__("Diamonds", "♦️")
