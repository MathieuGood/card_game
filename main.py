from entities.hand import Hand
from entities.deck import Deck
from entities.cards.card import Card
from entities.ranks.jack import Jack
from entities.ranks.king import King
from entities.ranks.queen import Queen
from entities.ranks.number_rank import NumberRank
from entities.suits.clubs import Clubs
from entities.suits.diamonds import Diamonds
from entities.suits.hearts import Hearts
from entities.suits.spades import Spades


deck = Deck()
print(deck)
# deck.print_all_cards()

spades = Spades()
king = King()

three = NumberRank(3)
hearts = Hearts()

king_spades = Card(king, spades)
three_hearts = Card(three, hearts)

hand = Hand()
# hand.add(deck.deal(5))
hand.add(
    [three_hearts, king_spades, three_hearts, three_hearts, three_hearts, three_hearts]
)

# hand.add([king_spades, three_hearts])
print(hand)

# drawn_card = hand.draw(0)
# print(hand)

hand.move_before(1, 3)
print(hand)
