from entities.ranks.face_rank import FaceRank


class King(FaceRank):

    def __init__(self) -> None:
        super().__init__("King", "K", 10)
