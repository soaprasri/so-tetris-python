from config.board_config import BoardConfig
from board.so_mino_helper import generate_new_shape, move_shape
from typing import Type
import logging

logging.basicConfig( 
level=logging.INFO, 
format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

logger = logging.getLogger(__name__)

class Mino():
    """ Main DDD class for the Mino(tetris shape on the board)
    """
    def __init__(self, board) -> None:
        self._board = board
        self._mino_x_pos_list = []
        self._mino_y_pos_list = []
        self._mino_color = 0
        pass

    def spawn(self):
        next_mino = generate_new_shape()
        if(self.__is_mino_allowed_on_board(next_mino)):
            self._mino_color = next_mino[0]
            self._mino_x_pos_list = next_mino[1]
            self._mino_y_pos_list = next_mino[2]
            self.__update_board()
            logger.info("SPAWNED NEXT MINO AND UPDATED BOARD")
            return True
        logger.debug(f"next_mino => {next_mino}")
        return False

    def __update_board(self):
        for i in range(4):
            self._board[self._mino_x_pos_list[i]][self._mino_y_pos_list[i]
                                                  ].active == BoardConfig.TYPE_FILLED_ACTIVE
            self._board[self._mino_x_pos_list[i]
                        ][self._mino_y_pos_list[i]].color == self._mino_color

    def __is_mino_allowed_on_board(self, mino):
        for i in range(4):
            cell_x = mino[1][i]
            cell_y = mino[2][i]
            if(self._board[cell_x][cell_y].active == True):
                return False
        return True

    def move(self, direction: int):
        next_shape = move_shape(self._mino_x_pos_list, self._mino_y_pos_list, direction)
            
        next_shape_x = next_shape[0]
        next_shape_y = next_shape[1]

        move_allowed = self.__is_move_allowed(next_shape_x, next_shape_y)

        logger.debug("move_allowed => " + str(move_allowed))

        if(move_allowed):
            # logger.info("update hot cells pos by => x="+ str(x) + " and y=" + str(y))
            self.__move(next_shape_x, next_shape_y)

        return move_allowed
   
    
    def __move(self, next_shape_x_pos_list: list[int], next_shape_y_pos_list: list[int]):
        for i in range(4):
            self._board[self._mino_x_pos_list[i]
                        ][self._mino_y_pos_list[i]].color = BoardConfig.COL_EMPTY
            self._board[self._mino_x_pos_list[i]
                        ][self._mino_y_pos_list[i]].active = BoardConfig.TYPE_EMPTY

        for i in range(4):
            self._mino_x_pos_list[i] = next_shape_x_pos_list[i]
            self._mino_y_pos_list[i] = next_shape_y_pos_list[i]

        for i in range(4):
            self._board[self._mino_x_pos_list[i]
                        ][self._mino_y_pos_list[i]].color = self._mino_color
            self._board[self._mino_x_pos_list[i]
                        ][self._mino_y_pos_list[i]].active = BoardConfig.TYPE_FILLED_ACTIVE

    def __is_move_allowed(self, next_shape_x: list[int], next_shape_y: list[int]):
        for i in range(4):
            logger.debug(f"is_move_allowed => {i}")
            next_x = next_shape_x[i]
            next_y = next_shape_y[i]

            if(next_y >= 0 and next_y <= BoardConfig.board_max_row - 1
                and next_x >= 0 and next_x <= BoardConfig.board_max_col - 1
                and (self._board[next_x][next_y].active == BoardConfig.TYPE_EMPTY
                     or self._board[next_x][next_y].active == BoardConfig.TYPE_FILLED_ACTIVE)):
                continue
            else:
                return False
        return True
        
    def freeze(self):
        for i in range(4):
            self._board[self._mino_x_pos_list[i]
                        ][self._mino_y_pos_list[i]].active = BoardConfig.TYPE_FILLED_INACTIVE
