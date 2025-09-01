from entities.cards.card import Card
from entities.playable_hands.playable_hand import PlayableHand


class Pair(PlayableHand):

    def __init__(self, cards: list[Card]) -> None:
        name = "Pair"
        if len(cards) != 2:
            raise ValueError(
                f"{name} should be instantiated with 2 cards, not {len(cards)}."
            )
        super().__init__(name, cards)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Pair):
            self.cards.sort(key=lambda card: (card.value, card.suit.symbol))
            value.cards.sort(key=lambda card: (card.value, card.suit.symbol))
            return self.cards == value.cards
        else:
            return False
