import numpy as np
from tensorflow import keras
import tensorflow as tf
from PIL import Image
from python.utils.classes import Char

from os import environ,chdir

environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
chdir("/home/yolo/Schreibtisch/Schularchivierer")




# loads the label file as an TextIOWrapper
label_file = open("ai/char_classification/label/label.txt","r")

# reads all trained classes from the label file
class_names = sorted([x.strip() for x in label_file.readlines()])

# loads the trained model
trained_model = keras.models.load_model("ai/char_classification/trained_model")

# makes a classification using the trained model

def make_classification(liste_images,img_name,regi_name,regi_bbox,regi_scale,regi_dist,chars):

    # load the input image and resizes it 
    # reshape it to the input size of the trained model

    liste_images = [img.resize((20, 20), Image.NEAREST) for img in liste_images]
    liste_images = tf.convert_to_tensor([np.reshape(img, (20, 20, 3)) for img in liste_images])

    liste_chars = []

    # makes the actual classification
    predictions = trained_model.predict_on_batch(liste_images)

    for prediction,char_bbox in zip(predictions,chars):

        # calculates the score of the classification
        score = tf.nn.softmax(prediction)
        
        # returns the label for the input image
        label = class_names[np.argmax(score)]
        
        liste_chars.append(Char(img_name,regi_name,regi_bbox,regi_scale,regi_dist,char_bbox,label))

    return liste_chars
    

