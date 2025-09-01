from entities.cards.card import Card
from entities.playable_hands.playable_hand import PlayableHand


class Pair(PlayableHand):

    def __init__(self, cards: list[Card]) -> None:
        if len(cards) != 2:
            raise ValueError(
                f"A pair should be instantiated with 2 cards, not {len(cards)}."
            )
        super().__init__("Pair", cards)
