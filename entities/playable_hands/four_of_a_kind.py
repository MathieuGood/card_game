from entities.cards.card import Card
from entities.playable_hands.playable_hand import PlayableHand


class FourOfAKind(PlayableHand):

    def __init__(self, cards: list[Card]) -> None:
        name = "Four of a Kind"
        if len(cards) != 4:
            raise ValueError(
                f"{name} should be instantiated with 3 cards, not {len(cards)}."
            )
        super().__init__(name, cards)
