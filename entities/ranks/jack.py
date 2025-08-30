from entities.ranks.face_rank import FaceRank


class Jack(FaceRank):

    def __init__(self) -> None:
        super().__init__("Jack", "J", 10)
