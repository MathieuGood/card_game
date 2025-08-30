# from entities.ranks.jack import Jack
# from entities.ranks.queen import Queen
# from entities.ranks.king import King

from entities.ranks.rank import Rank


class FaceRank(Rank):

    def __init__(self, name: str, symbol: str, value: int) -> None:
        super().__init__(name, symbol, value)
