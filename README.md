# so-tetris-python
Tetris Demo
- Quick attempt to demo OOPS and DDD in python
    -  Initial rough code is present in so-tetris-python/so-dev/so_tetris_dev_full.py
    -  Later refactored the code as per OOPS recommendations.
    -  Many items are still pending for calling it full-fledged game and can be taken up as time permits.
    
- Dependencies => pygame
- Dev Env => VSCode on macOS Big Sur
    
    
- DDD Description
    -  All the configurations in config directory
        - board_config
        - display_config
    -  Game app is divided into Display and Board
        - Display is for managing pygame aspects - Display of screen elements and capturing/handling of events
        - Board is the Gameplay code encapsulating the -
            - logical board, 
            - minos(shapes) - their movement,
            - metadata - game score etc.
            
    -  Display code is in display dir
        - so_display - all the screen elements and pygame lib management
        - so_event_listener - receives all the events on screen and redirects activities to appropriate modules
        - so_display_helper - isolated utility methods for display module
        
    -  Board logic is in board dir
        - so_board - DDD logical model for the Tetris board hosting all the cells and their properties
        - so_mino - DDD logical model for tetris minos.
            i. minos are the shapes spawned at the top which then move down till they are stopped by inactive cells.
            ii. This has methods for movement - LRB, rotation etc.
        - so_mino_helper - Hosts static utility functions for rotation and spawning of new minos(shapes)
        - so_metadata - stores the game data for score state etc.
         
    -  Lauch of the app is from this file -
            python3 so-tetris-python/so_tetris_mania.py >> logs.txt 2>&1
            
    -  Logger used - can configure to direct logs to specific file as per deployment.
    
    -  All the pending TODOs are captured in so_tetris_mania.py
