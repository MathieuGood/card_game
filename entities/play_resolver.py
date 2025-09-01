from entities.card_containers.card_container import CardContainer
from entities.cards.card import Card
from entities.playable_hands.pair import Pair


class PlayResolver:

    playable_hands = []

    def __init__(self, card_container: CardContainer) -> None:
        self.card_container = card_container

    def find_pairs(self) -> list[Pair]:
        found_pairs: list[Pair] = []
        for card1 in self.card_container.cards:
            for card2 in self.card_container.cards:
                if card1.equal_rank(card2) and card1 is not card2:
                    found_pair: Pair = Pair([card1, card2])
                    if found_pair not in found_pairs:
                        found_pairs.append(found_pair)
                        print(f"Pair : {card1} and {card2}")
        return found_pairs
