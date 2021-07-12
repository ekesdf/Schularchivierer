import sys

sys.path.insert(0, "/home/yolo/Schreibtisch/Schularchivierer")

from multiprocessing import Pool

from ai.char_classification.python.classify_chars import make_classification
from ai.char_localization.python.detect_char import make_char_detection


cwd2 = "temp/images/text_regions/" 


def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(2) as p:
       print(p.map(f, [1, 2, 3]))


for region in img.textregions:

    print(region.name)
        
    chars,time_chars_detection = make_char_detection(cwd2+image_name+"/"+region.name)

    liste_chars_cutout = cut_image(chars,cwd2+image_name+"/"+region.name,"char")

    for index in range(len(liste_chars_cutout)):

        char_image = liste_chars_cutout[index]
        char_bbox = chars[index]
        label = make_classification(char_image)
        char = Char(img.name,region.name,region.bbox,region.scale,region.dist,char_bbox,label[0])
        liste_chars.append(char)

    count_chars += len(chars) 