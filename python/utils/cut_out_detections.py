from PIL.Image import open as open_image
from os import mkdir
from shutil import rmtree
from os.path import exists


def cut_image(list_detections, image_path, mode):

    img = open_image(image_path)
    img_name = image_path.split("/")[len(image_path.split("/"))-1]
    index = 0
    liste_images = []

    if exists("temp/images/"+mode+"s/"+img_name):

        rmtree("temp/images/"+mode+"s/"+img_name)
        mkdir("temp/images/"+mode+"s/"+img_name)

    else: mkdir("temp/images/"+mode+"s/"+img_name)


    for detection in list_detections:

        temp = img.crop(tuple(detection))
        liste_images.append(temp)
        temp.save("temp/images/"+mode+"s/"+img_name+"/"+str(index)+".jpg")
        index += 1

    return liste_images
    
