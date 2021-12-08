
from numpy import interp

def calculate_position_of_char_in_the_pdf(image_shape,pdf_shape,coordinates):

    x = round(interp(coordinates[0],[0,image_shape[0]],[0,pdf_shape[0]]))
    y = round(interp(coordinates[1],[0,image_shape[1]],[0,pdf_shape[1]]))

    return int(round(x)), int(round(y))