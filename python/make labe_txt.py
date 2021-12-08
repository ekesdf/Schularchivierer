
from os import listdir

txt = open("/home/yolo/Schreibtisch/Schularchivierer/ai/char_classification/label/label.txt","w")

path = "/home/yolo/Schreibtisch/custom_model/classification/Char-detection/dataset"

for folder in listdir(path): txt.write(folder+"\n")

txt.close()