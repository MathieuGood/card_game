from entities.cards.card import Card


class CardContainer:

    def __init__(self, size: int):
        self.cards: list[Card] = []
        self.size = size
        self.name: str = "Container"

    def __repr__(self) -> str:
        return f"{self.name} with {len(self.cards)} cards:\n" + "\n".join(
            str(card) for card in enumerate(self.cards)
        )

    def add(self, cards: Card | list[Card]):
        if isinstance(cards, list):
            self.cards.extend(cards)
        elif isinstance(cards, Card):
            self.cards.append(cards)
        else:
            raise ValueError("Invalid type, must be Card or list of Card")

    def draw(self, card_index: int) -> Card:
        return self.cards.pop(card_index)

    def move_after(self, card_index_to_move: int, card_index_to_move_after: int):
        card_to_move: Card = self.cards.pop(card_index_to_move)
        self.cards.insert(card_index_to_move_after, card_to_move)

    def move_before(self, card_index_to_move: int, card_index_to_move_before: int):
        card_to_move: Card = self.cards.pop(card_index_to_move)
        self.cards.insert(card_index_to_move_before - 1, card_to_move)
