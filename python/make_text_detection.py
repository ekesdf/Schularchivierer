# -*- coding: utf-8 -*-


from os import chdir, environ
from sys import path

from tensorflow import config

###                  ###
# setting configvalues #
###                  ###
environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
chdir("/home/yolo/Schreibtisch/Schularchivierer")
path.insert(0, "/home/yolo/Schreibtisch/Schularchivierer")
gpus = config.list_physical_devices('GPU')
config.experimental.set_memory_growth(gpus[0], True)
config.experimental.set_memory_growth(gpus[1], True)



from time import process_time, time

from ai.char_classification.python.classify_chars import make_classification
from ai.char_localization.python.detect_char import make_char_detection
from ai.text_region_localization.python.detect_region import make_region_detection

from python.utils.classes import Image, Textregion
from python.utils.functions import (clear_temp_folder, cut_image, normalize_text_regions,
                                    write_char_into_the_grid, write_chars_into_txt)

count_chars = 0
cwd2 = "temp/images/text_regions/" 
temp = []
liste_chars = []

###                                           ###
# INPUT_PATH to the image you want to detect on #
###                                           ###
image_path = "input/test.jpg"


###                                              ###
# Deletes all the existing folders and             #
# files in the temp folder to improve Memory usage #
###                                              ###
clear_temp_folder()

###                                                      ###                                         
# Converts a file path with the format "home/*/*/*/*/*.jpg #
# in to the corresponding filename with the format "*.jpg" #
###                                                      ###
image_name = image_path.split("/")[len(image_path.split("/"))-1]


###                                                                                  ###
# Detects the regions of texts in the image read from the given image_path.            #
# Returns a 2 Array of ints with the given format [[x1,y1,x2,y2],[x1, y1, x2, y2],...] #
# and the time in seconds it took to predict the regions                               #
###                                                                                  ###                                                                              
text_regions,time_regions_detection,image_shape = make_region_detection(image_path)


print(f"\nThe model has detected {len(text_regions)} text regions in {round(time_regions_detection,6)} seconds\n")

###                                                                      ###
# Get the current time used for calculating the time,                      #
# the programme needed to detect and classify all chars in all textregions #
###                                                                      ###
start_char_detection = time()

###                                                                                                    ###
# Gets a 2 Array of ints with the given format [[x1,y1,x2,y2],[x1, y1, x2, y2],...]                      #
# and cuts the regions out and stores them in the temp folder under temp/images/chars/NAME_OF_THE_REGION #
# returns a list of PIL.Image objects of the cut out regions                                             #
###                                                                                                    ###                                                                     
liste_images = cut_image(text_regions,image_path,"text_region")

###                                                                                                          ###
# Gets a list of PIL.image objects with a variable size and pastes each individual image in to a 832x832 image #
# with a red bacackground. If the give image exeeds the 832 limit in any direction it will be sized to 832.    # 
# The image is positioned in the center of the other image with its own center.                                #
###                                                                                                          ###
dict_scale_factors,dist = normalize_text_regions(liste_images,image_name)



###                                                       ###                             
# Loops trough the list of regions and greats list with the #
# corresponding Texregion objects                           #
# The list has the format [Textregion,Textregion,...]       #
###                                                       ###
for index in range(len(text_regions)):

    bbox = text_regions[index]
    scale = dict_scale_factors[index]
    distance = dist[index]
    region_name = str("normalized "+str(index)+".jpg")

    temp.append(Textregion(image_name,region_name,bbox,scale,distance))

### ###
#     #
### ###

img = Image(image_name,image_shape,temp)

### ###
#     #
### ###

for region in img.textregions:
     
    chars,time_chars_detection = make_char_detection(cwd2+image_name+"/"+region.name)

    liste_chars_cutout = cut_image(chars,cwd2+image_name+"/"+region.name,"char")

    liste_chars += make_classification(liste_chars_cutout,img.name,region.name,region.bbox,region.scale,region.dist,chars)

    count_chars += len(chars) 


print(f"\nThe model has detected {count_chars} Chars in {round(time()-start_char_detection,6)} seconds.\n")

### ###
#     #
### ###

grid = write_char_into_the_grid(liste_chars)
write_chars_into_txt(grid)

print(f"To translate the Site took {process_time()} seconds\n")    
