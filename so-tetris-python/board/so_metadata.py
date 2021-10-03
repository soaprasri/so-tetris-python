
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

logger = logging.getLogger(__name__)

class GameData():
    """Game Metadata
    """

    def __init__(self) -> None:
        self._completed_rows = 0
        self._game_over = False

    def on_rows_completed(self, count: int):
        self._completed_rows = self._completed_rows + count
        logger.info(f"TOTAL SCORE TILL NOW => {self._completed_rows}")

    def on_game_completed(self):
        self._game_over = True
