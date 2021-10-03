"""[summary]
    
    Board 
        array of cells - game field
        hot cells - minos
        movement of cells
        delete complete row
        update score
"""
from config.board_config import BoardConfig
from board.so_mino import Mino
from board.so_metadata import GameData
from board.so_board_cell import BoardCell
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

logger = logging.getLogger(__name__)


class Board():

    def __init__(self) -> None:
        self._board = [[BoardCell.empty() for y in range(BoardConfig.board_max_row)]
                       for x in range(BoardConfig.board_max_col)]
        self.__spawn_next_mino()
        self._game_data = GameData()
        self._game_over = False

    @property
    def board(self):
        return self._board

    @property
    def game_over(self):
        return self._game_over

    # @property
    # def game_data(self):
    #     return self._game_data

    def __spawn_next_mino(self):
        self._mino = Mino(self._board)
        success = self._mino.spawn()
        if(not success):
            logger.info("Could not spawn Mino, GAME OVER!!")
            self._game_over = True

    def move(self, direction: int):
        if(self._game_over):
            logger.info("GAME OVER!!")
            return

        success = self._mino.move(direction)
        if(direction == BoardConfig.DIRECTION_DOWN and not success):
            self.__invalidate()

        # check if move possible
            # y - move
            # n - freeze mino
            # n - check if rows completed
            # y - delete row
            # y - update score
            # n - spawn_next_mino
        pass

    def __invalidate(self):
        logger.info("Invalidate board requested!!")
        self._mino.freeze()
        count = self.__remove_completed_rows()
        self._game_data.on_rows_completed(count)
        self.__spawn_next_mino()
        pass

    def __remove_completed_rows(self):
        count = 0
        for y in range(0, BoardConfig.board_max_row):
            completed = True
            for x in range(0, BoardConfig.board_max_col):
                if(self._board[x][y].active == BoardConfig.TYPE_EMPTY):
                    completed = False

            if(completed == True):
                self.__remove_row(y)
                count = count + 1
        return count

    def __remove_row(self, row_num: int):
        for y in range(row_num, 1, -1):
            for x in range(0, BoardConfig.board_max_col-1):

                self._board[x][y].color = self._board[x][y-1].color
                self._board[x][y].active = self._board[x][y-1].active

        for x in range(0, BoardConfig.board_max_col-1):
            self._board[x][0].color = BoardConfig.TYPE_EMPTY
            self._board[x][0].active = BoardConfig.COL_EMPTY

    def game_over(self):
        #        self._game_data.on_game_completed()
        self._game_over = True
