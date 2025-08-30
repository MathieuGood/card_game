from entities.cards.card import Card
from entities.suits.suit import Suit


class NumberCard(Card):

    def __init__(self, suit: Suit, rank: str, value: int):
        super().__init__(suit, rank, value)
