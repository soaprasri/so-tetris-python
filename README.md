# so-tetris-python
Tetris Demo
- Quick attempt to demo OOPS and DDD in python
        -  Initial rough code is present in so-tetris-python/so-dev/so_tetris_dev_full.py
        -  Later refactored the code as per OOPS recommendations.
        -  Many items are still pending for calling it full-fledged game and can be taken up as time permits.
    
- Dependencies => pygame
- Dev Env => VSCode on macOS Big Sur
    
    
- DDD Description
    0.  All the configurations in config directory
        a) board_config
        b) display_config
    1.  Game app is divided into Display and Board
        a) Display is for managing pygame aspects - Display of screen elements and capturing/handling of events
        b) Board is the Gameplay code encapsulating the -
            i. logical board, 
            ii. minos(shapes) - their movement,
            iii. metadata - game score etc.
            
    2.  Display code is in display dir
        a) so_display - all the screen elements and pygame lib management
        b) so_event_listener - receives all the events on screen and redirects activities to appropriate modules
        c) so_display_helper - isolated utility methods for display module
        
    3.  Board logic is in board dir
        a) so_board - DDD logical model for the Tetris board hosting all the cells and their properties
        b) so_mino - DDD logical model for tetris minos.
            i. minos are the shapes spawned at the top which then move down till they are stopped by inactive cells.
            ii. This has methods for movement - LRB, rotation etc.
        c) so_mino_helper - Hosts static utility functions for rotation and spawning of new minos(shapes)
        d) so_metadata - stores the game data for score state etc.
         
    4.  Lauch of the app is from this file -
            python3 so-tetris-python/so_tetris_mania.py >> logs.txt 2>&1
            
    5.  Logger used - can configure to direct logs to specific file as per deployment.
    
    6. All the pending TODOs are captured in so_tetris_mania.py
