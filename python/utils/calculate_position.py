
from numpy import interp

def calculate_position_of_char_in_the_pdf(image_shape,pdf_shape,coordinates):

    image_width = image_shape[0]
    image_height = image_shape[1]
    pdf_width = pdf_shape[0]
    pdf_height = pdf_shape[1]
    x = coordinates[0]
    y = coordinates[1]

#    corrected_x = round(interp(x,[0,image_width],[0,pdf_width]))
#    corrected_y = round(interp(y,[0,image_height],[0,pdf_height]))


    if x % 1 > 0.5: corrected_x = round(x)-1

    else: corrected_x = round(x)

    if y % 1 > 0.5: corrected_y =round(y)-1

    else: corrected_y =round(y)


    return corrected_x, corrected_y