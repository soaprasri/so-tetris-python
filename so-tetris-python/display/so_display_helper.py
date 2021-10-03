from config.board_config import BoardConfig
from config.display_config import DisplayConfig

def get_cell_color_from_code(cell_color_code):
    if(cell_color_code == BoardConfig.COL_RED):
        cell_color = (DisplayConfig.RED)
    elif(cell_color_code == BoardConfig.COL_YELLOW):
        cell_color = (DisplayConfig.YELLOW)
    elif(cell_color_code == BoardConfig.COL_GREEN):
        cell_color = (DisplayConfig.GREEN)
    elif(cell_color_code == BoardConfig.COL_BLUE):
        cell_color = (DisplayConfig.BLUE)
    elif(cell_color_code == BoardConfig.COL_ORANGE):
        cell_color = (DisplayConfig.ORANGE)
    elif(cell_color_code == BoardConfig.COL_PURPLE):
        cell_color = (DisplayConfig.PURPLE)
    elif(cell_color_code == BoardConfig.COL_CYAN):
        cell_color = (DisplayConfig.CYAN)
    elif(cell_color_code == BoardConfig.COL_EMPTY
            or cell_color_code == 0):
        cell_color = (DisplayConfig.BLACK)
    return cell_color