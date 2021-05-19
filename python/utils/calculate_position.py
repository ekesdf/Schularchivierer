
from numpy import interp

def calculate_position_of_char_in_the_pdf(image_shape,pdf_shape,coordinates):

    image_width = image_shape[0]
    image_height = image_shape[1]
    pdf_width = pdf_shape[0]
    pdf_height = pdf_shape[1]
    x = coordinates[0]
    y = coordinates[1]

    corrected_x = interp(x,[0,image_width],[0,pdf_width])
    corrected_y = interp(y,[0,image_height],[0,pdf_height])

    return corrected_x, corrected_y