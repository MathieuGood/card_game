from entities.cards.card import Card


class PlayableHand:

    def __init__(self, name: str, cards: list[Card]) -> None:
        self.name = name
        self.cards = cards

    def __repr__(self) -> str:
        return f"{self.name} with {len(self.cards)} cards: \n" + "\n".join(
            str(card) for card in enumerate(self.cards)
        )
