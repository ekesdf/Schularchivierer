import sys
sys.path.insert(0, "/home/yolo/Schreibtisch/Schularchivierer")

from numpy import interp

cols = 70
rows = 50


grid = [[" " for _ in range(cols)] for _ in range(rows) ]


def interpolating_pos(inp_y, inp_x):
    '''Interpolates the given Pos of the char in the image to the actual pos in the PDF'''

    out_y = interp(inp_y, [0, 3484], [1, 580]) 
    out_x = interp(inp_x, [0, 2397], [1, 210]) 
    out_y = interp(out_y, [0, 400 ], [1, 69 ]) 
    out_x = interp(out_x, [0, 210 ], [1, 49 ]) 

    out_y = int(out_y)
    out_x = int(out_x)

    return out_y, out_x

def write_char_into_the_grid(liste_chars):

    for char in liste_chars:

        char_x = char.normalized_x1+round((char.normalized_x2 - char.normalized_x1) / 2)
        char_y = char.normalized_y1+round((char.normalized_y2 - char.normalized_y1) / 2)
        
        char_row,char_col = interpolating_pos(char_x,char_y)
        grid[char_col][char_row] = char.label

    return grid
    
def write_chars_into_txt(grid):

    out = open('test.txt', 'w')

    for index, row in enumerate(grid):

        row_str = "".join(" " if col == "" else col for col in row)

        if index <= len(grid): out.write(row_str+"\n")

        else: out.write(row_str)
