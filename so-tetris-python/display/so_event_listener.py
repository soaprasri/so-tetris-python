import pygame
from config.board_config import BoardConfig
import logging

logging.basicConfig( 
level=logging.INFO, 
format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

logger = logging.getLogger(__name__)

class TetrisEventListener():
    """PyGame events listener
    
    Receives all pygame events and pushes them to appropriate modules
    """
    def __init__(self, board) -> None:
        self.board = board
        self.app_exit = False
        self.current_game_over = False
        
    def on_event(self, event):
        if(event.type == pygame.QUIT):
            self.app_exit = True
            logger.info("User requesting QUIT!!")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self.board.move(BoardConfig.DIRECTION_UP)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.board.move(BoardConfig.DIRECTION_DOWN)
                pass
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.board.move(BoardConfig.DIRECTION_LEFT)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.board.move(BoardConfig.DIRECTION_RIGHT)
        return (self.app_exit, self.current_game_over)