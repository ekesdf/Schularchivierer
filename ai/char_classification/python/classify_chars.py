from os import chdir, environ

from numpy import reshape as np_reshape, argmax as np_argmax 
from PIL.Image import NEAREST
from tensorflow import convert_to_tensor
from tensorflow.keras.models import load_model
from tensorflow.python.keras.backend import softmax

from python.utils.classes import Char

environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
chdir("/home/yolo/Schreibtisch/Schularchivierer")



# loads the label file as an TextIOWrapper
label_file = open("ai/char_classification/label/label.txt","r")

# reads all trained classes from the label file
class_names = sorted([x.strip() for x in label_file.readlines()])

# loads the trained model
trained_model = load_model("ai/char_classification/trained_model")

# makes a classification using the trained model

def make_classification(liste_images,img_name,regi_name,regi_bbox,regi_scale,regi_dist,chars):

    # load the input image and resizes it 
    # reshape it to the input size of the trained model

    liste_images = [img.resize((20, 20), NEAREST) for img in liste_images]
    liste_images = convert_to_tensor([np_reshape(img, (20, 20, 3)) for img in liste_images])

    liste_chars = []

    # makes the actual classification
    predictions = trained_model.predict_on_batch(liste_images)

    for prediction,char_bbox in zip(predictions,chars):

        # calculates the score of the classification
        score = softmax(prediction)
        
        # returns the label for the input image
        label = class_names[np_argmax(score)]
        
        liste_chars.append(Char(img_name,regi_name,regi_bbox,regi_scale,regi_dist,char_bbox,label))

    return liste_chars
    

