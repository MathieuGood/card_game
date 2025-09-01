from entities.cards.card import Card
from entities.card_containers.card_container import CardContainer


class Hand(CardContainer):

    def __init__(self, size: int):
        super().__init__(size)
        self.name = "Hand"

    def __repr__(self) -> str:
        return super().__repr__()
