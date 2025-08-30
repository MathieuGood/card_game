from entities.suits.suit import Suit
from entities.suits.spades import Spades
from entities.suits.clubs import Clubs
from entities.suits.diamonds import Diamonds
from entities.suits.hearts import Hearts
from entities.ranks.rank import Rank


class Card:

    def __init__(self, rank: Rank, suit: Suit):
        if not isinstance(suit, (Spades, Clubs, Diamonds, Hearts)):
            raise ValueError(f"Invalid suit : {suit}")
        if not isinstance(rank, Rank):
            raise ValueError(f"Invalid rank : {rank}")

        self.value = rank.value
        self.suit = suit
        self.rank = rank

    def is_greater_than(self, other_card: "Card"):
        return self.value > other_card.value

    def __repr__(self) -> str:
        return f"{self.rank} {self.suit}"

    def __eq__(self, value: object) -> bool:
        return (
            isinstance(value, Card)
            and self.suit == value.suit
            and self.rank == value.rank
        )
