import random
from config.board_config import BoardConfig
import logging

logging.basicConfig( 
level=logging.INFO, 
format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')

logger = logging.getLogger(__name__)



def generate_new_shape():
    """Generate new shape
        #0: 
        hot_cell_y = [0,1,2,3] 
        hot_cell_x = [5,5,5,5]
        X
        X
        X
        X

        #1: 
        hot_cell_y = [0,0,0,0]
        hot_cell_x = [3,4,5,6]
        XXXX

        #2:
        hot_cell_y = [0,1,0,1]  
        hot_cell_x = [4,4,5,5]
        XX
        XX

        #3.
        hot_cell_y = [0,0,1,1]  
        hot_cell_x = [4,5,5,6] 
        XX
         XX

        #4.
        hot_cell_y = [0,1,1,2]  
        hot_cell_x = [4,4,5,5] 
        X
        XX
         X

        #5.
        hot_cell_y = [0,1,2,2]  
        hot_cell_x = [4,4,4,5]
        X
        X
        XX

        #6.
        hot_cell_y = [1,0,1,1]  
        hot_cell_x = [4,4,5,6]
          X
        XXX
    """
    shape_id = random.randint(1, 7)
    logger.info("generating shape id => " + str(shape_id))

    shape_color = shape_id

    if(shape_id == 2):
        shape_y_pos_list = [0, 0, 0, 0]
        shape_x_pos_list = [3, 4, 5, 6]
    elif(shape_id == 3):
        shape_y_pos_list = [0, 1, 0, 1]
        shape_x_pos_list = [4, 4, 5, 5]
    elif(shape_id == 4):
        shape_y_pos_list = [0, 0, 1, 1]
        shape_x_pos_list = [4, 5, 5, 6]
    elif(shape_id == 5):
        shape_y_pos_list = [0, 1, 1, 2]
        shape_x_pos_list = [4, 4, 5, 5]
    elif(shape_id == 6):
        shape_y_pos_list = [0, 1, 2, 2]
        shape_x_pos_list = [4, 4, 4, 5]
    elif(shape_id == 7):
        shape_y_pos_list = [0, 1, 1, 1]
        shape_x_pos_list = [4, 4, 5, 6]
    else:
        shape_y_pos_list = [0, 1, 2, 3]
        shape_x_pos_list = [5, 5, 5, 5]

    return (shape_color, shape_x_pos_list, shape_y_pos_list)

def rotate_shape(shape_x_pos_list, shape_y_pos_list):
        """
        hot_cell_y = [0,1,1,2]  
            hot_cell_x = [4,4,5,5] 
            X               0,0
            XX              0,1 1,1
             X                  1,2

             0

        find mid of x series
        find mid of y series

            for all x values -> find diff of value from mid value
            from mid fo y series
                use the diff of x values to populate the y values
            ^^ repeat for all y values.
        """
        
        sum_x_pos = 0
        sum_y_pos = 0
        for i in range(4):
            sum_x_pos = sum_x_pos + shape_x_pos_list[i]
            sum_y_pos = sum_y_pos + shape_y_pos_list[i]

        # avg_x_pos = round(sum_x_pos/4)
        # avg_y_pos = round(sum_y_pos/4)
        avg_x_pos = int(sum_x_pos/4)
        avg_y_pos = int(sum_y_pos/4)

        
        next_mino_x_pos_list = [0] * 4
        next_mino_y_pos_list = [0] * 4

        for i in range(4):
            x_shift_from_mid = shape_x_pos_list[i] - avg_x_pos
            next_mino_y_pos_list[i] = avg_y_pos + x_shift_from_mid

            y_shift_from_mid = shape_y_pos_list[i] - avg_y_pos
            next_mino_x_pos_list[i] = avg_x_pos + y_shift_from_mid
        
        return (next_mino_x_pos_list, next_mino_y_pos_list)
    
def move_shape(shape_x_pos_list, shape_y_pos_list, direction):
    """Move shape to next steps

    Args:
        shape_x_pos_list ([type]): [description]
        shape_y_pos_list ([type]): [description]
        direction ([type]): [description]

    Returns:
        [type]: [description]
    """
    move_x = 0
    move_y = 0
    
    if(direction == BoardConfig.DIRECTION_UP):
            next_shape = rotate_shape(shape_x_pos_list, shape_y_pos_list)
    
    else: 
        if(direction == BoardConfig.DIRECTION_DOWN):
            move_x = 0
            move_y = 1
        elif(direction == BoardConfig.DIRECTION_LEFT):
            move_x = -1
            move_y = 0
        if(direction == BoardConfig.DIRECTION_RIGHT):
            move_x = 1
            move_y = 0

        next_shape_x = [0] * 4
        next_shape_y = [0] * 4
        for i in range(4):
            logger.debug(f"is_move_allowed => {i}")
            next_shape_x[i] = shape_x_pos_list[i] + move_x
            next_shape_y[i] = shape_y_pos_list[i] + move_y
        next_shape = (next_shape_x, next_shape_y)
        
    return next_shape
