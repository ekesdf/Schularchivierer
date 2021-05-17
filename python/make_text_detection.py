import sys
from os import system,listdir,environ
from time import time

environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

translate_start = time()
sys.path.insert(0, "/home/yolo/Schreibtisch/Schularchivierer")



from ai.char_classification.python.classify_chars import make_classification
from ai.char_localization.python.detect_char import make_char_detection
from ai.text_region_localization.python.detect_region import make_region_detection
from python.utils.cut_out_detections import cut_image
from python.utils.make_char_annotations import make_char_annotations
from python.utils.make_text_region_annotations import make_text_region_annotations
from python.utils.normalize_text_regions import normalize_text_regions 
from python.utils.classes import Image,Textregion,Char


count_chars = 0
cwd2 = "temp/images/text_regions/" 
cwd3 = "temp/images/chars/"










image_path = "input/img-00400.jpg"
image_name = image_path.split("/")[len(image_path.split("/"))-1]

text_regions,time_regions_detection,shape_image = make_region_detection(image_path)




print()
print(f"The model has detected {len(text_regions)} text regions in {round(time_regions_detection,6)} seconds\n")

# Detecting all the Textregions and normalize them for the Chardetection and further processing
# writes the annotation for the corresponding Textregion.

liste_images = cut_image(text_regions,image_path,"text_region")
dict_scale_factors,dist = normalize_text_regions(liste_images,image_name)
start_char_detection = time()

temp = []
for index in range(len(text_regions)):

    temp.append(Textregion(image_name,str("normalized "+str(index)+".jpg"),text_regions[index],dict_scale_factors[index],dist[index]))

img = Image(image_name,shape_image,temp)

liste_chars = []

for region in img.textregions:

    print(region.name)
        
    chars,time_chars_detection = make_char_detection(cwd2+image_name+"/"+region.name)

    liste_chars_cutout = cut_image(chars,cwd2+image_name+"/"+region.name,"char")

    for index in range(len(liste_chars_cutout)):

        char_image = liste_chars_cutout[index]
        char_bbox = chars[index]

        label = make_classification(char_image)
        char = Char(img.name,region.name,region.bbox,region.scale,region.dist,char_bbox,label)
        liste_chars.append(char)


    
    count_chars += len(chars) 

# print(liste_chars)

print(f"The model has detected {count_chars} Chars in {round(time()-start_char_detection,6)} seconds.\n")

for char in liste_chars:

    if char.bbox[0] < 0  or char.bbox[1] < 0 or char.bbox[2] < 0 or char.bbox[3]:
        
        print(char.bbox)
        print(char.textregion_bbox)



# print(f"To translate the Site took {round(time()-translate_start,6)} seconds\n")