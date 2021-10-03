import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 30  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (180, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 180)
BOARD_COLOR = BLUE
SCREEN_COLOR = WHITE

screen = pygame.display.set_mode((800,800))
screen.fill(SCREEN_COLOR)
image = pygame.image.load(r'/Users/soaprateek/Downloads/20440546.bmp')
done = False # make it false to start display

board_array =  [[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0]]  
board_max_row = 20
board_max_col = 10

logger.info("board_array[0][0] =>", str(board_array[1][1]))
board_array[1][1] = 1  
logger.info("board_array[0][0] =>", str(board_array[1][1]))


# traversing the board
for i in range (0, board_max_row):
    for j in range(0, board_max_col):
        logger.info(board_array[i][j])

# render the board
cell_size = 30

def render_board():
    cell_size = 30
    board_start_pos_x = 200
    board_start_pos_y = 10
    for i in range (0, board_max_row):
        for j in range(0, board_max_col):
            cell_color = (GREEN)
            if(board_array[i][j] == 0):
                cell_color = (RED)
            elif(board_array[i][j] == 2):
                cell_color = (BLUE)
            pygame.draw.rect(screen, cell_color, pygame.Rect(board_start_pos_x + (30 * j),
                                                                board_start_pos_y  + (30 * i),
                                                                28,
                                                                28))
hot_cell_y = 0
hot_cell_x = 5

def spawn_again():
    global hot_cell_y, hot_cell_x 
    board_array[hot_cell_y][hot_cell_x] = 1
    hot_cell_y = 0
    hot_cell_x = 5
    if(board_array[hot_cell_y][hot_cell_x]):
        logger.info("GAME OVER!!")
        exit()

#
def move(direction):
    logger.info("move " + str(direction))
    global hot_cell_x, hot_cell_y
    if(direction == pygame.K_UP):
        if(hot_cell_y > 0 and board_array[hot_cell_y-1][hot_cell_x] == 0):
            board_array[hot_cell_y][hot_cell_x] = 0
            hot_cell_y = hot_cell_y-1
    elif(direction == pygame.K_DOWN):
        if(hot_cell_y < board_max_row -1 and board_array[hot_cell_y+1][hot_cell_x] == 0):
            board_array[hot_cell_y][hot_cell_x] = 0
            hot_cell_y = hot_cell_y+1
        else: 
            spawn_again()
    elif(direction == pygame.K_LEFT):
        if(hot_cell_x > 0 and board_array[hot_cell_y][hot_cell_x-1] == 0):
            board_array[hot_cell_y][hot_cell_x] = 0
            hot_cell_x = hot_cell_x-1
    if(direction == pygame.K_RIGHT):
        if(hot_cell_x < board_max_col -1 and board_array[hot_cell_y][hot_cell_x+1] == 0):
            board_array[hot_cell_y][hot_cell_x] = 0
            hot_cell_x = hot_cell_x+1
    
    board_array[hot_cell_y][hot_cell_x] = 2



last_ms = 0
move_down_tick = 200
i = 10
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                move(pygame.K_UP)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                move(pygame.K_DOWN)
                pass
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                move(pygame.K_LEFT)
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                move(pygame.K_RIGHT)

    current_ms = pygame.time.get_ticks()
    logger.debug("current_ms=" + str(current_ms))
    if(current_ms - last_ms > move_down_tick):
        move(pygame.K_DOWN)
        last_ms = current_ms

    screen.fill(SCREEN_COLOR)
    screen.blit(image,(0,0))
    pygame.draw.rect(screen, (GREEN), pygame.Rect(30+i,30+i,30,30))
    pygame.draw.rect(screen, (RED), pygame.Rect(0,0,30,30))
    render_board()
    i = i+ 1
    pygame.display.flip()



"""
    Let us do rough work here.

    We need 10X20 board ~ 10 squares X 20 squares

    Store info in a 2d array.

    We should be able to draw board based on that array.

    cell values - 0,1,2
    - 0 = empty
    - 1 = fixed cells
    - 2 = movable cells

    



    """