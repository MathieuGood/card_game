from entities.suits.suit import Suit


class Clubs(Suit):

    def __init__(self) -> None:
        super().__init__("Clubs", "♣️")
