from PIL import Image

img = Image.open("/home/yolo/Schreibtisch/Schularchivierer/input/img-00400.jpg")

img.crop((1310,1595,1331,1631)).save("test.jpg")