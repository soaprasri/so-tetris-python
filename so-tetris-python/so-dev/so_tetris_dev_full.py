import pygame
import random

pygame.init()


clock = pygame.time.Clock()
FPS = 30  # Frames per second.

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
INACTIVE_CELLS_COLOR = pygame.Color("#00a8e8") #pygame.Color("#007ea7")
BOARD_COLOR = BLUE
SCREEN_COLOR = pygame.Color("#ffffff")

COL_RED = 7
COL_YELLOW = 1
COL_GREEN = 2
COL_CYAN = 3
COL_ORANGE = 4
COL_PURPLE = 5
COL_BLUE = 6


screen = pygame.display.set_mode((1200,800))
screen.fill(SCREEN_COLOR)
image = pygame.image.load(r'/Users/soaprateek/Downloads/blue_bg.bmp')
image = pygame.transform.scale(image, (1200, 800))
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
                [0,0,0,0,0,0,0,0,0,0],
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
        logger.debug(board_array[i][j])
        pass

# render the board
cell_size = 30

def render_board():
    cell_size = 30
    board_start_pos_x = 200
    board_start_pos_y = 10
    for i in range (0, board_max_row):
        for j in range(0, board_max_col):
            cell_color = (BLACK)
            if(abs(board_array[i][j]) == COL_RED):
                cell_color = (RED)
            elif(abs(board_array[i][j]) == COL_YELLOW):
                cell_color = (YELLOW)
            elif(abs(board_array[i][j]) == COL_GREEN):
                 cell_color = (GREEN)
            elif(abs(board_array[i][j]) == COL_BLUE):
                 cell_color = (BLUE)
            elif(abs(board_array[i][j]) == COL_ORANGE):
                cell_color = (ORANGE)
            elif(abs(board_array[i][j]) == COL_PURPLE):
                cell_color = (PURPLE)
            elif(abs(board_array[i][j]) == COL_CYAN):
                 cell_color = (CYAN)
            elif(abs(board_array[i][j]) == 0):
                 cell_color = (BLACK)
            else:
                logger.info("using default color, could not find color for col code = " + str(board_array[i][j]))
            
            pygame.draw.rect(screen, cell_color, pygame.Rect(board_start_pos_x + (34 * j),
                                                                board_start_pos_y  + (34 * i),
                                                                33,
                                                                33))

hot_cell_y = [0,1,2,3]
hot_cell_x = [5,5,5,5]
hot_color = COL_GREEN

def delete_row(row_num):
    for i in range(row_num, 0, -1):
            for j in range(0, board_max_col):
                board_array[i][j] = board_array[i-1][j]
    
    for j in range(0, board_max_col):
                board_array[0][j] = 0


def show_hot_cells():
    for i in range(4):
        board_array[hot_cell_y[i]][hot_cell_x[i]] = hot_color

    # for cell_x in hot_cell_x:
    #     for cell_y in hot_cell_y:
    #         logger.debug("("+ str(cell_y)+ "," + str(cell_x)+") = 2")
    #         board_array[cell_y][cell_x] = 2

score = 0
def increment_score():
    global score
    score = score+1
    logger.info("current_score => ", str(score))
def delete_full_rows():
    for i in range (0, board_max_row):
        completed = True
        for j in range(0, board_max_col):
            if(board_array[i][j] == 0):
                completed = False
        if(completed == True):
            increment_score()
            # delete row
            delete_row(i)



def spawn_again():
    global hot_cell_y, hot_cell_x
    freeze_hot_cells()
    delete_full_rows()
    spawn_new_hot_cells()

def get_new_hot_cells():
    """Generate new shape
        #0: hot_cell_y = [0,1,2,3] hot_cell_x = [5,5,5,5]
        X
        X
        X
        X

        #1: hot_cell_y = [5,5,5,5] hot_cell_x = [0,1,2,3]
        XXXX

        #2: hot_cell_y = [0,1,0,1]  hot_cell_x = [4,4,5,5] 
        XX
        XX

        3. hot_cell_y = [0,0,1,1]  hot_cell_x = [4,5,5,6] 
        XX
         XX

        4. hot_cell_y = [0,1,1,2]  hot_cell_x = [4,4,5,5] 
        X
        XX
         X

        5. hot_cell_y = [0,1,2,2]  hot_cell_x = [4,4,4,5] 
        X
        X
        XX

        6. hot_cell_y = [0,1,1,1]  hot_cell_x = [4,4,5,6] 
        X
        XXX


    """
    global hot_cell_y, hot_cell_x, hot_color

    shape_num =  random.randint(1,7)
    logger.info("generating shape no. " + str(shape_num))

    if(shape_num == 7):
        hot_cell_y = [0,1,2,3] 
        hot_cell_x = [5,5,5,5]
    elif(shape_num == 1):
        hot_cell_y = [0,0,0,0]
        hot_cell_x = [3,4,5,6]
    elif(shape_num == 2):
        hot_cell_y = [0,1,0,1]  
        hot_cell_x = [4,4,5,5]
    elif(shape_num == 3):
        hot_cell_y = [0,0,1,1]  
        hot_cell_x = [4,5,5,6] 
    elif(shape_num == 4):
        hot_cell_y = [0,1,1,2]  
        hot_cell_x = [4,4,5,5] 
    elif(shape_num == 5):
        hot_cell_y = [0,1,2,2]  
        hot_cell_x = [4,4,4,5]
    elif(shape_num == 6):
        hot_cell_y = [0,1,1,1]  
        hot_cell_x = [4,4,5,6]
    
    hot_color = shape_num

    for cell_x in hot_cell_x:
        for cell_y in hot_cell_y:
            if(board_array[cell_y][cell_x] != 0):
                logger.info("GAME OVER!!")
                exit()
    
    show_hot_cells()

get_new_hot_cells()



def spawn_new_hot_cells():
    get_new_hot_cells()

def get_new_hot_color():
    global hot_color
    hot_color = COL_GREEN            

def freeze_hot_cells():
    for i in range(4):
        board_array[hot_cell_y[i]][hot_cell_x[i]] = -1 * board_array[hot_cell_y[i]][hot_cell_x[i]]

#
def move(direction):
    logger.debug("move " + str(direction))
    global hot_cell_x, hot_cell_y
    if(direction == pygame.K_UP):
        try_moving_hot_cells(0,-1)
    elif(direction == pygame.K_DOWN):
        success = try_moving_hot_cells(0,1)
        if(not success):
            spawn_again()
    elif(direction == pygame.K_LEFT):
        try_moving_hot_cells(-1,0)
    if(direction == pygame.K_RIGHT):
        try_moving_hot_cells(1,0)

def try_moving_hot_cells(x,y):
    global hot_cell_x, hot_cell_y
    #left x =1
    move_allowed = True
    for i in range(4):
            if(hot_cell_y[i] + y >= 0 
            and hot_cell_y[i] + y <= board_max_row -1 
            and hot_cell_x[i] + x >= 0 
            and hot_cell_x[i] + x <= board_max_col -1 
            and (board_array[hot_cell_y[i] + y][hot_cell_x[i] + x] == 0 or board_array[hot_cell_y[i] + y][hot_cell_x[i] + x] == hot_color)):
                pass
            else:
                move_allowed = False
    logger.debug("move_allowed => " + str(move_allowed))
    if(move_allowed):
        logger.debug("update hot cells pos by => x="+ str(x) + " and y=" + str(y))
        old_hot_cell_x = [0,0,0,0]
        old_hot_cell_y = [0,0,0,0]

        for i in range(4):
            old_hot_cell_x[i] = hot_cell_x[i]
            old_hot_cell_y[i] = hot_cell_y[i]

            hot_cell_x[i] = hot_cell_x[i] + x
            hot_cell_y[i] = hot_cell_y[i] + y
            board_array[old_hot_cell_y[i]][old_hot_cell_x[i]] = 0

        for i in range(4):
            board_array[hot_cell_y[i]][hot_cell_x[i]] = hot_color
            logger.debug("hot_cell_y[i] =>" + str(hot_cell_y[i]) + ", [hot_cell_x[i]] =>" +  str(hot_cell_x[i]))
            logger.debug("old_hot_cell_y[i] =>" + str(old_hot_cell_y[i]) + ", [old_hot_cell_x[i]] =>" + str(old_hot_cell_x[i]))


        #show_hot_cells()
    return move_allowed









last_ms = 0
move_down_tick = 500
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