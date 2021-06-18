
from numpy import interp

def calculate_position_of_char_in_the_pdf(image_shape,pdf_shape,coordinates):

    x = round(interp(coordinates[0],[0,image_shape[0]],[0,pdf_shape[0]]))
    y = round(interp(coordinates[1],[0,image_shape[1]],[0,pdf_shape[1]]))

    if x % 1 > 0.5: corrected_x = round(x)-1

    else: corrected_x = round(x)

    if y % 1 > 0.5: corrected_y =round(y)-1

    else: corrected_y =round(y)


    return corrected_x, corrected_y