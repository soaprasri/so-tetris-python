from config.board_config import BoardConfig
from config.display_config import DisplayConfig
from board.so_board import Board
from display.so_display_helper import get_cell_color_from_code
import logging

logging.basicConfig( 
level=logging.INFO, 
format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

logger = logging.getLogger(__name__)

class Display():
    """Display module for the Tetris demo using pygame
    """
    def __init__(self, pygame, board) -> None:
        self.pygame = pygame
        self.board = board
        self.__display_context_init()
        pass
    def __display_context_init(self):
        self.screen = self.pygame.display.set_mode(
            (DisplayConfig.SCREEN_WIDTH, DisplayConfig.SCREEN_HEIGHT))

        image = self.pygame.image.load(DisplayConfig.BG_IMAGE)
        self.image = self.pygame.transform.scale(
            image, (DisplayConfig.SCREEN_WIDTH, DisplayConfig.SCREEN_HEIGHT))
    
    def invalidate(self):
        self.screen.fill(self.pygame.Color(DisplayConfig.SCREEN_COLOR))
        self.screen.blit(self.image, (0, 0))

        self.__render_board(self.board)
        self.pygame.display.flip()
    
    def __render_board(self, board: Board):
        cell_size = DisplayConfig.BOARD_CELL_SIZE
        board_start_pos_x = DisplayConfig.BOARD_X
        board_start_pos_y = DisplayConfig.BOARD_Y

        for x in range(BoardConfig.board_max_col):
            for y in range(BoardConfig.board_max_row):
                cell_color_code = self.board.board[x][y].color
                cell_color = get_cell_color_from_code(cell_color_code)
                if(cell_color == None):
                    cell_color = (DisplayConfig.BLACK)
                    logger.info(f" For ({x},{y}) using default color,\
                        as col code not found => {cell_color_code}")

                self.pygame.draw.rect(self.screen, cell_color,
                                self.pygame.Rect(board_start_pos_x + ((DisplayConfig.BOARD_CELL_SIZE - 1) * x),
                                            board_start_pos_y +((DisplayConfig.BOARD_CELL_SIZE - 1) * y),
                                            (DisplayConfig.BOARD_CELL_SIZE - 2),
                                            (DisplayConfig.BOARD_CELL_SIZE - 2)))
    


