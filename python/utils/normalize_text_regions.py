from PIL import Image
from os import listdir

cwd = "temp/images/text_regions/"

def normalize_text_regions(liste_images,image_name):

    index = 0
    liste_textregions = []
    liste_dist = []

    for text_region in liste_images:

        new_text_region = Image.new("RGB",(832,832),"red")
        temp_size = text_region.size
        if text_region.size[0] > 832 and text_region.size[1] > 832: text_region = text_region.resize((832,832),Image.NEAREST)
        elif text_region.size[0] > 832: text_region = text_region.resize((832,text_region.size[1]))
        elif text_region.size[1] > 832: text_region = text_region.resize((text_region.size[0],832))

        dist_left = round((832-text_region.size[0])/2)
        dist_top  = round((832-text_region.size[1])/2)

        new_text_region.paste(text_region,(dist_left,dist_top))

        new_text_region.save(cwd+image_name+"/normalized "+str(index)+".jpg")

        index += 1
        # print((temp_size[1]/832,temp_size[0]/832))
        # print("\n")
        liste_textregions.append((temp_size[0]/832,temp_size[1]/832))
        liste_dist.append((dist_left,dist_top))
    
    return liste_textregions,liste_dist