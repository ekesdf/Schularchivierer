import functiontrace
functiontrace.trace()
import sys
sys.path.insert(0, "/home/yolo/Schreibtisch/Schularchivierer")



from python.utils.classes import Grid,Cell
from python.utils.calculate_position import calculate_position_of_char_in_the_pdf

cols = 42
rows = 59
pdf_w = 210
pdf_h = 297

cell_w = pdf_w / cols
cell_h = pdf_h / rows

grid = Grid(rows=rows, cols=cols,cell_w=cell_w,cell_h=cell_h).make_grid()

def write_char_into_the_grid(liste_chars):

    for char in liste_chars:

        char_x = char.normalized_x1+round((char.normalized_x2 - char.normalized_x1) / 2)
        char_y = char.normalized_y1+round((char.normalized_y2 - char.normalized_y1) / 2)

        # char_x = char.normalized_x1
        # char_y = char.normalized_y1

        char_row,char_col = calculate_position_of_char_in_the_pdf((2397,3484),(cols,rows),(char_x,char_y))

        grid[char_col-1][char_row-1] = char.label

    return grid










