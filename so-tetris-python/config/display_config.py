class AppConfig():
    pass    

class DisplayConfig():
    """All the configs for tuning the Tetris game display
    """
    #Screen Configs
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 780

    BG_IMAGE = r'../../images/so-blue-bg.bmp'
    # BG_IMAGE = r'/Users/soaprateek/Downloads/Untitled.bmp'

    #Board Configs
    BOARD_X = 250
    BOARD_Y = 30
    BOARD_CELL_SIZE = 35 

    #Mino move down tick
    MOVE_DOWN_TICK = 500
    
     #display
    FPS = 30  # Frames per second.

    #Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 127, 0)
    PURPLE = (128, 0, 128)
    CYAN = (0, 255, 255)

    ACTIVE_CELLS_COLOR = RED #pygame.Color("#ee6c4d")
    INACTIVE_CELLS_COLOR = "#00a8e8" #pygame.Color("#007ea7")
    BOARD_COLOR = BLUE
    SCREEN_COLOR = "#ffffff"
