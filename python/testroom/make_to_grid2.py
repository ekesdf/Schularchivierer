from numpy import interp

# 297x210
290 * 2 = 580

def interpolating_pos(inp_y, inp_x):
    
    '''Interpolates the given Pos of the char in the image to the actual pos in the PDF'''

    out_y = interp(inp_y,[0,3484],[1,580])
    out_x = interp(inp_x,[0,2397],[1,420])

    return out_y, out_x
    
