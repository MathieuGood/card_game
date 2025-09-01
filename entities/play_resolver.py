from entities.card_containers.card_container import CardContainer
from entities.cards.card import Card
from entities.playable_hands.four_of_a_kind import FourOfAKind
from entities.playable_hands.pair import Pair
from entities.playable_hands.playable_hand import PlayableHand
from entities.playable_hands.three_of_a_kind import ThreeOfAKind


class PlayResolver:

    def __init__(self, card_container: CardContainer) -> None:
        self.card_container = card_container
        self.resolved_hands: list[PlayableHand] = []

    def get_hand_value(self, hand: PlayableHand) -> int:
        total_value = 0
        for card in hand.cards:
            total_value += card.value
        return total_value

    def find_pair(self) -> None:
        found_pairs: list[Pair] = []
        for card1 in self.card_container.cards:
            for card2 in self.card_container.cards:
                if card1.equal_rank(card2) and card1 is not card2:
                    found_pair: Pair = Pair([card1, card2])
                    if found_pair not in found_pairs:
                        found_pairs.append(found_pair)
        self.resolved_hands.extend(found_pairs)

    def find_three_of_a_kind(self) -> None:
        found_three_of_a_kinds: list[ThreeOfAKind] = []
        for card1 in self.card_container.cards:
            for card2 in self.card_container.cards:
                for card3 in self.card_container.cards:
                    if (
                        card1.equal_rank(card2)
                        and card1.equal_rank(card3)
                        and card1 is not card2
                        and card1 is not card3
                        and card2 is not card3
                    ):
                        found_three_of_a_kind: ThreeOfAKind = ThreeOfAKind(
                            [card1, card2, card3]
                        )
                        if found_three_of_a_kind not in found_three_of_a_kinds:
                            found_three_of_a_kinds.append(found_three_of_a_kind)
        self.resolved_hands.extend(found_three_of_a_kinds)

    def find_four_of_a_kind(self) -> None:
        found_four_of_a_kinds: list[FourOfAKind] = []
        for card1 in self.card_container.cards:
            for card2 in self.card_container.cards:
                for card3 in self.card_container.cards:
                    for card4 in self.card_container.cards:
                        if (
                            card1.equal_rank(card2)
                            and card1.equal_rank(card3)
                            and card1.equal_rank(card4)
                            and card1 is not card2
                            and card1 is not card3
                            and card1 is not card4
                            and card2 is not card3
                            and card2 is not card4
                            and card3 is not card4
                        ):
                            found_four_of_a_kind: FourOfAKind = FourOfAKind(
                                [card1, card2, card3, card4]
                            )
                            if found_four_of_a_kind not in found_four_of_a_kinds:
                                found_four_of_a_kinds.append(found_four_of_a_kind)
                                print(
                                    f"Four of a Kind : {card1}, {card2}, {card3} and {card4}"
                                )
        self.resolved_hands.extend(found_four_of_a_kinds)

    def keep_playable_hands(self) -> None:
        playable_hands = []
        used_cards = []

        # Sort hands by value in descending order (highest value first)
        sorted_hands = sorted(
            self.resolved_hands, key=lambda hand: hand.value, reverse=True
        )

        for hand in sorted_hands:
            # Check if any card in this hand is already used
            has_overlap = False
            for card in hand.cards:
                if card in used_cards:
                    has_overlap = True
                    break

            if not has_overlap:
                # No overlap with already used cards, so we can add this hand
                playable_hands.append(hand)
                used_cards.extend(hand.cards)

        self.resolved_hands = playable_hands
