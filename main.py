from entities.card_containers.hand import Hand
from entities.deck import Deck
from entities.cards.card import Card
from entities.play_resolver import PlayResolver
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
hearts = Hearts()
diamonds = Diamonds()
clubs = Clubs()

king = King()
queen = Queen()

three = NumberRank(3)


king_spades = Card(king, spades)
king_hearts = Card(king, hearts)
queen_diamonds = Card(queen, diamonds)
three_hearts = Card(three, hearts)
three_hearts2 = Card(three, hearts)
three_spades = Card(three, spades)
three_clubs = Card(three, clubs)
three_diamonds = Card(three, diamonds)


hand = Hand(10)
# hand.add(deck.deal(5))
hand.add([king_hearts, queen_diamonds, three_spades, three_clubs, three_diamonds])

print(hand)


play_resolver = PlayResolver(hand)
print(play_resolver.find_pairs())
