from multiprocessing import Pool
from os import mkdir
from os.path import exists
from shutil import rmtree

from numpy import interp
from PIL.Image import open as open_image, new as new_Image, NEAREST

cols = 70
rows = 50

grid = [[" " for _ in range(cols)] for _ in range(rows) ]

path = "temp/images/"
cwd = "temp/images/text_regions/"

def clear_temp_folder():

    rmtree("temp/images")
    mkdir("temp/images")
    mkdir("temp/images/chars")
    mkdir("temp/images/text_regions")

def cut(data):

    detection,img,mode,img_name,index = data

    temp = img.crop(tuple(detection))

    temp.save(path+mode+"s/"+img_name+"/"+str(index)+".jpg")

    return temp

def cut_image(list_detections, image_path, mode):

    """
    Gets a 2 Array of ints with the given format [[x1,y1,x2,y2],[x1, y1, x2, y2],...]\n
    and cuts the regions out and stores them in the temp folder under temp/images/text_regions/NAME_OF_THE_REGION.\n
    Returns a list of PIL.Image objects of the cut out regions
    """

    img = open_image(image_path)
    img_name = image_path.split("/")[len(image_path.split("/"))-1]
    liste_images = []

    if exists(path+mode+"s/"+img_name): rmtree(path+mode+"s/"+img_name)

    mkdir(path+mode+"s/"+img_name)

    if len(list_detections) > 0:

        pool = Pool(round((len(list_detections)+0.5)/2))

        liste_images = pool.map(cut,zip(list_detections,
                                    [img for _ in range(len(list_detections))],
                                    [mode for _ in range(len(list_detections))],
                                    [img_name for _ in range(len(list_detections))],
                                    [index for index in range(len(list_detections))]
                                    ))

    return liste_images



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



def normalize(data):

    text_region,image_name,index = data

    new_text_region = new_Image("RGB",(832,832),"red")
    temp_size = text_region.size

    if text_region.size[0] > 832 and text_region.size[1] > 832: text_region = text_region.resize((832,832),NEAREST)
    elif text_region.size[0] > 832: text_region = text_region.resize((832,text_region.size[1]))
    elif text_region.size[1] > 832: text_region = text_region.resize((text_region.size[0],832))

    dist_left = round((832-text_region.size[0])/2)
    dist_top  = round((832-text_region.size[1])/2)

    new_text_region.paste(text_region,(dist_left,dist_top))

    new_text_region.save(cwd+image_name+"/normalized "+str(index)+".jpg")

    index += 1

    return (temp_size[0]/832,temp_size[1]/832),(dist_left,dist_top)


def normalize_text_regions(liste_images,image_name):

    """
    Gets a list of PIL.image objects with a variable size and pastes each individual image in to a 832x832 image\n
    with a red bacackground. If the give image exeeds the 832 limit in any direction it will be sized to 832.\n
    The image is positioned in the center of the other image with its own center.
    """

    # index = 0
    liste_scale_factors = []
    liste_dist = []


    pool = Pool(round(len(liste_images)+0.5/2))


    results = pool.map(normalize,
                       zip(liste_images,
                          [image_name for _ in range(len(liste_images))],
                           range(len(liste_images))))

    for result in results:

        liste_scale_factors.append(result[0])
        liste_dist.append(result[1])

    return liste_scale_factors,liste_dist