from PIL.Image import open as open_image
from os import mkdir
from shutil import rmtree
from os.path import exists
from multiprocessing import Pool

path = "temp/images/"


def cut(data):

    detection,img,mode,img_name,index = data

    temp = img.crop(tuple(detection))

    temp.save(path+mode+"s/"+img_name+"/"+str(index)+".jpg")
    index += 1

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

    if exists(path+mode+"s/"+img_name):

        rmtree(path+mode+"s/"+img_name)
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
    
