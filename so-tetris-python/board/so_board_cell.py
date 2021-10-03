from config.board_config import BoardConfig

class BoardCell():
    def __init__(self, color: int, active: int) -> None:
        self._color = color
        self._active = active
        pass

    @property
    def color(self):
        return self._color

    @property
    def active(self):
        return self._active

    @color.setter
    def color(self, a):
        self._color = a

    @active.setter
    def active(self, a):
        self._active = a
        
    @classmethod
    def empty(cls):
        return cls(BoardConfig.COL_EMPTY, BoardConfig.TYPE_EMPTY)