import pygame

from board.so_board import Board
from config.board_config import BoardConfig
from config.display_config import DisplayConfig
from display.so_event_listener import TetrisEventListener
from display.so_display import Display 

import logging

logging.basicConfig( 
level=logging.INFO, 
format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class TetrisMania():
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self._board = Board()
        self._display = Display(pygame, self._board)
        self._event_listener = TetrisEventListener(self._board)
        
        self.last_ms = 0
        self.app_exit = False
        self.current_game_over = False

    def run(self):
        while not self.app_exit:
            self.clock.tick(DisplayConfig.FPS)
            self.__handle_events()
            self.__next_step()
            self._display.invalidate()

        logger.info("Exiting...See you soon!!")

    def __next_step(self):
        current_ms = pygame.time.get_ticks()
        if(current_ms - self.last_ms > DisplayConfig.MOVE_DOWN_TICK):
            self._board.move(BoardConfig.DIRECTION_DOWN)
            self.last_ms = current_ms

    def __handle_events(self):
        for event in pygame.event.get():
            app_status = self._event_listener.on_event(event)
            self. app_exit = app_status[0]
            self.current_game_over = app_status[1]


if __name__ == "__main__":
    logger.info("starting tetris game app!!")
    TetrisMania().run()
    

"""TODO -
        Read oops in python -
        static, class structure
        #private methods, static methods, class methods
        #private methods start with __(two underscores)
        #static methods for similar to java utility static methods - utility methods
        #class methods for factory - returning specific class objects.
        assigning types to parameters
        moudle creation
        logging
        documentation
        github
        try in pycharm = NOOOOO
        
        if possible ->
        next shape -> display somewhere
        one line delay while rendering
        display of fonts + score etc.
        
    """