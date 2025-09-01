from entities.cards.card import Card


class PlayableHand:

    def __init__(self, name: str, cards: list[Card]) -> None:
        self.name = name
        self.cards = cards
        self.value = self.calculate_value()

    def __repr__(self) -> str:
        # print(f"{self.name} with {len(self.cards)} cards:")
        # for hand in self.cards:
        #     print(hand)
        return (
            f"{self.name} with {len(self.cards)} cards | "
            + " | ".join(str(card) for card in self.cards)
            + f" | {self.value} points"
        )

    def calculate_value(self) -> int:
        total_value = 0
        for card in self.cards:
            total_value += card.value
        return total_value

    def __eq__(self, value: object) -> bool:
        if isinstance(value, PlayableHand):
            self.cards.sort(key=lambda card: (card.rank.value, card.suit.symbol))
            value.cards.sort(key=lambda card: (card.rank.value, card.suit.symbol))
            return self.cards == value.cards
        else:
            return False
