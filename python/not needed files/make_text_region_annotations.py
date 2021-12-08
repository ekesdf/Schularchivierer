from os import mkdir
from shutil import rmtree
from os.path import exists
from PIL.Image import open as open_image

path = "temp/annotations/"

def make_text_region_annotations(liste_detections,image_name,mode):

    

    if exists(path+mode+"s/"+image_name): rmtree(path+mode+"s/"+image_name)

    mkdir(path+mode+"s/"+image_name)

    for index, detection in enumerate(liste_detections):

        with open(path+mode+"s/"+image_name+"/"+str(index)+".txt","w") as file:

            if mode == "text_region":

                width,height = open_image("temp/images/text_regions/"+image_name+"/"+str(index)+".jpg").size
                scale_x,scale_y = width/832,height/832
                file.write(f"{detection[0]} {detection[1]} \
                             {detection[2]} {detection[3]} \
                             {scale_x} {scale_y} {image_name}")

            else: file.write(f"{detection[0]} {detection[1]} {detection[2]} {detection[3]}")