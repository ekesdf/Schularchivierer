import numpy as np
from tensorflow import keras
import tensorflow as tf
from PIL import Image


# loads the label file as an TextIOWrapper
label_file = open("ai/char_classification/label/label.txt","r")

# reads all trained classes from the label file
class_names = sorted([x.strip() for x in label_file.readlines()])

# loads the trained model
trained_model = keras.models.load_model("ai/char_classification/trained_model")

# makes a classification using the trained model
def make_classification(img):

    # load the input image and resizes it 
    img = np.asarray(img.resize((20, 20), Image.NEAREST))
    # reshape it to the input size of the trained model
    img = np.reshape(img, (1, 20, 20, 3))

    # makes the actual classification
    predictions = trained_model.predict(img)

    # calculates the score of the classification
    score = tf.nn.softmax(predictions[0])
    
    # returns the label for the input image
    label = class_names[np.argmax(score)]
    
    return label,score
    

