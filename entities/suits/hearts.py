from entities.suits.suit import Suit


class Hearts(Suit):

    def __init__(self) -> None:
        super().__init__("Hearts", "♥️")
