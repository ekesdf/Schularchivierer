from PIL.Image import new as new_Image, NEAREST
from multiprocessing import Pool

cwd = "temp/images/text_regions/"


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


    results = pool.map(normalize, zip(liste_images,[image_name for _ in range(len(liste_images))], range(len(liste_images))))

    for result in results:

        liste_scale_factors.append(result[0])
        liste_dist.append(result[1])

    # for text_region in liste_images:

        # new_text_region = Image.new("RGB",(832,832),"red")
        # temp_size = text_region.size
        # if text_region.size[0] > 832 and text_region.size[1] > 832: text_region = text_region.resize((832,832),Image.NEAREST)
        # elif text_region.size[0] > 832: text_region = text_region.resize((832,text_region.size[1]))
        # elif text_region.size[1] > 832: text_region = text_region.resize((text_region.size[0],832))

        # dist_left = round((832-text_region.size[0])/2)
        # dist_top  = round((832-text_region.size[1])/2)

        # new_text_region.paste(text_region,(dist_left,dist_top))

        # new_text_region.save(cwd+image_name+"/normalized "+str(index)+".jpg")

        # index += 1

        # liste_textregions.append((temp_size[0]/832,temp_size[1]/832))
        # liste_dist.append((dist_left,dist_top))
    
    return liste_scale_factors,liste_dist