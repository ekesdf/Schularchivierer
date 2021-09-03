from numpy import interp


def interpolating_pos(inp_y, inp_x):
    '''Interpolates the given Pos of the char in the image to the actual pos in the PDF'''

    out_y = interp(inp_y, [0, 3484], [1, 580]) 
    out_x = interp(inp_x, [0, 2397], [1, 210]) 
    out_y = interp(out_y, [0, 400 ], [1, 69 ]) 
    out_x = interp(out_x, [0, 210 ], [1, 49 ]) 

    out_y = int(out_y)
    out_x = int(out_x)

    return out_y, out_x

def write_chars_into_txt(grid):

    out = open('test.txt', 'w')

    for index, row in enumerate(grid):

        row_str = "".join(" " if col == "" else col for col in row)

        if index <= len(grid): out.write(row_str+"\n")

        else: out.write(row_str)
