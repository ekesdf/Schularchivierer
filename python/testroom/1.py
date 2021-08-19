import numpy as np
import time,cv2,os



CONFIG_FILE  = "ai/char_localization/trained_model/detect_v2.cfg"
WEIGHTS_FILE = "ai/char_localization/trained_model/detect_v2.weights"
CONFIDENCE_THRESHOLD = 0.8
WIDTH = 832
HEIGHT = 832



net = cv2.dnn.readNetFromDarknet(CONFIG_FILE, WEIGHTS_FILE)

test = os.listdir("temp/images/text_regions/test0003.jpeg")
test = ["temp/images/text_regions/test0003.jpeg/"+i for i in test if "normalized" in i]

def make_char_detection(image_path):



    # initialize our lists of detected bounding boxes, confidences, and
    # class IDs, respectively
    boxes = []
    confidences = []
    results = []

    images = [cv2.imread(path) for path in image_path]

    (H, W) = images[0].shape[:2]

    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]


    blob = cv2.dnn.blobFromImages(images, 1 / 255.0, (WIDTH, HEIGHT),swapRB=True, crop=False)

    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    end = time.time()


    # loop over each of the layer outputs
    for output in layerOutputs:
        
        # loop over each of the detections
        for detection in output:
            
            k = 0
            # # extract the class ID and confidence (i.e., probability) of
            # # the current object detection
            # scores = detection[][5:]
            # classID = np.argmax(scores)
            # confidence = scores[classID]

            # # filter out weak predictions by ensuring the detected
            # # probability is greater than the minimum probability
            # if confidence > CONFIDENCE_THRESHOLD:

            #     # scale the bounding box coordinates back relative to the
            #     # size of the image, keeping in mind that YOLO actually
            #     # returns the center (x, y)-coordinates of the bounding
            #     # box followed by the boxes' width and height
            #     box = detection[0:4] * np.array([W, H, W, H])
            #     (centerX, centerY, width, height) = box.astype("int")

            #     # use the center (x, y)-coordinates to derive the top and
            #     # and left corner of the bounding box
            #     x = int(centerX - (width / 2))
            #     y = int(centerY - (height / 2))

            #     # update our list of bounding box coordinates, confidences,
            #     # and class IDs
            #     boxes.append([x, y, int(width), int(height)])
            #     confidences.append(float(confidence))

make_char_detection(test)