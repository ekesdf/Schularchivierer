from shutil import rmtree
from os import mkdir

def clear_temp_folder():


    rmtree("temp/images")
    mkdir("temp/images")
    mkdir("temp/images/chars")
    mkdir("temp/images/text_regions")