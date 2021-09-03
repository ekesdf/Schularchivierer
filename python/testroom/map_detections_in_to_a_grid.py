
import sys
sys.path.insert(0, "/home/yolo/Schreibtisch/Schularchivierer")

from python.utils.classes import Grid
from python.testroom.make_to_grid2 import interpolating_pos

cols = 70
rows = 50


grid = [[" " for _ in range(cols)] for _ in range(rows) ]

def write_char_into_the_grid(liste_chars):

    for char in liste_chars:

        char_x = char.normalized_x1+round((char.normalized_x2 - char.normalized_x1) / 2)
        char_y = char.normalized_y1+round((char.normalized_y2 - char.normalized_y1) / 2)
        
        char_row,char_col = interpolating_pos(char_x,char_y)
        # print(char_row,char_col)
        grid[char_col][char_row] = char.label

    return grid










