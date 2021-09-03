from numpy import interp


# Test locations of chars detected in a Image.

# [663, 183, 704, 254]
# [176, 385, 220, 430]
# [449, 527, 515, 610]
# [396, 182, 449, 251]
# [142, 251, 192, 309]
# [436, 581, 489, 623]
# [271, 382, 318, 442]
# [520, 452, 557, 486]
# [621, 337, 665, 403]
# [530, 332, 567, 401]

# 3508 x 2480


def interpolating_pos(inp_y, inp_x):
    
    '''Interpolates the given Pos of the char in the image to the actual pos in the PDF'''

    out_y = interp(inp_y,[0,3484],[1,60])
    out_x = interp(inp_x,[0,2397],[1,71])
    out_y -= 0.5
    out_x -= 0.5 
    out_y = round(out_y)
    out_x = round(out_x)
    
    return out_y, out_x
    
pdf_y,pdf_x = interpolating_pos(663, 183)



