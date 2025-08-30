from entities.ranks.rank import Rank


class NumberRank(Rank):

    def __init__(self, value: int) -> None:
        if not (0 < value < 11):
            raise ValueError(f"{value} is not a correct number card value.")

        name = str(value)
        if value == 1:
            value = 11
            name = "Ace"

        super().__init__(name, name, value)
