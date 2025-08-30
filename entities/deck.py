from entities.cards.card import Card
from entities.ranks.jack import Jack
from entities.ranks.king import King
from entities.ranks.queen import Queen
from entities.ranks.number_rank import NumberRank
from entities.ranks.face_rank import FaceRank
from entities.suits.clubs import Clubs
from entities.suits.diamonds import Diamonds
from entities.suits.hearts import Hearts
from entities.suits.spades import Spades
from entities.suits.suit import Suit

import random


class Deck:

    face_ranks: list[FaceRank] = [King(), Queen(), Jack()]
    suits: list[Suit] = [Hearts(), Diamonds(), Spades(), Clubs()]

    def __init__(self) -> None:
        self._cards: list[Card] = []
        self.build_deck()
        self.shuffle()

    def build_deck(self) -> None:
        for face_rank in self.face_ranks:
            for suit in self.suits:
                self._cards.append(Card(face_rank, suit))

        for number in range(1, 11):
            for suit in self.suits:
                self._cards.append(Card(NumberRank(number), suit))

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def print_all_cards(self) -> None:
        print("Cards in this decks :")
        for card in self._cards:
            print(card)

    def deal(self, number: int = 1) -> list[Card]:
        if number > self.__len__():
            raise ValueError(
                f"Not enough cards remaining in the deck : {self.__len__()} left / {number} asked"
            )

        drawn_cards: list[Card] = []
        for i in range(number):
            drawn_cards.append(self._cards.pop(0))
        return drawn_cards

    def __len__(self) -> int:
        return len(self._cards)

    def __repr__(self) -> str:
        return f"Deck with {len(self._cards)} cards"
