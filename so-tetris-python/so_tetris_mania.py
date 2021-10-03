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
    """Tetris Game App Main class
    Quick attempt to demo OOPS and DDD in python
        1. Initial rough code is present in so-tetris-python/so-dev/so_tetris_dev_full.py
        2. Later refactored the code as per OOPS recommendations.
        3. Many items are still pending for calling it full-fledged game and can be taken up as time permits.
    
    Dependencies => pygame
    Dev Env => VSCode on macOS Big Sur
    
    
    DDD =>
    0. All the configurations in config directory
        a. board_config
        b. display_config
    1. Game app is divided into Display and Board
        a. Display is for managing pygame aspects - Display of screen elements and capturing/handling of events
        b. Board is the Gameplay code encapsulating the -
            i. logical board, 
            ii. minos(shapes) - their movement,
            iii. metadata - game score etc.
            
    2. Display code is in display dir
        a. so_display - all the screen elements and pygame lib management
        b. so_event_listener - receives all the events on screen and redirects activities to appropriate modules
        c. so_display_helper - isolated utility methods for display module
        
    3. Board logic is in board dir
        a. so_board - DDD logical model for the Tetris board hosting all the cells and their properties
        b. so_mino - DDD logical model for tetris minos.
            i. minos are the shapes spawned at the top which then move down till they are stopped by inactive cells.
            ii. This has methods for movement - LRB, rotation etc.
        c. so_mino_helper - Hosts static utility functions for rotation and spawning of new minos(shapes)
        d. so_metadata - stores the game data for score state etc.
         
    4. Lauch of the app is from this file -
            python3 so-tetris-python/so_tetris_mania.py >> logs.txt 2>&1
            
    5. Logger used - can configure to direct logs to specific file as per deployment.
    
    6. All the pending TODOs are captured in so_tetris_mania.py
    """
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
        # oops in python -
        # static, class structure
        # private methods, static methods, class methods
        # private methods start with __(two underscores)
        # static methods for similar to java utility static methods - utility methods
        # class methods for factory - returning specific class objects.
        assigning types to parameters
        module creation
        # logging
        # documentation - Added ReadMe and basic doc
        # github
        
        if possible ->
        Enhancement : next shape -> display somewhere
        Enhancement : Actual rotate on up key press
        Fix: one line delay while rendering
        Enhancement: display of fonts + score etc.
        
    """
