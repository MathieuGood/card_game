from entities.ranks.face_rank import FaceRank


class Queen(FaceRank):

    def __init__(self) -> None:
        super().__init__("Queen", "Q", 10)
