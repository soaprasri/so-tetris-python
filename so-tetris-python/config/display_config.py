class AppConfig():
    pass    

class DisplayConfig():
    #Screen Configs
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800

    BG_IMAGE = r'/Users/soaprateek/Downloads/blue_bg.bmp'

    #Board Configs
    BOARD_X = 200
    BOARD_Y = 10
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
