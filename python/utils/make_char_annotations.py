from os import mkdir,path
from shutil import rmtree


def make_char_annotations(liste_detections,image_path,mode):
    
    img_name = image_path.split("/")[len(image_path.split("/"))-1]
    index = 0

    if path.exists("temp/annotations/"+mode+"s/"+img_name):

        rmtree("temp/annotations/"+mode+"s/"+img_name)
        mkdir("temp/annotations/"+mode+"s/"+img_name)
    
    else: mkdir("temp/annotations/"+mode+"s/"+img_name)

    for detection in liste_detections:

        with open("temp/annotations/"+mode+"s/"+img_name+"/"+str(index)+".txt","w") as file:
                
            file.write(f"{detection[0]} {detection[1]} {detection[2]} {detection[3]}")

        index += 1