from numpy import array as np_array, argmax as np_argmax
from time import time
from cv2 import imread as cv2_imread
from cv2 import dnn

CONFIG_FILE = "ai/char_localization/trained_model/detect_v2.cfg"
WEIGHTS_FILE = "ai/char_localization/trained_model/detect_v2.weights"
CONFIDENCE_THRESHOLD = 0.8
WIDTH = 416
HEIGHT = 416

net = dnn.readNetFromDarknet(CONFIG_FILE, WEIGHTS_FILE)


def make_char_detection(region_path):
    """
    Gets a path to an textregion where the chars need to be localized
    """

    # initialize our lists of detected bounding boxes, confidences, and
    # class IDs, respectively
    boxes = []
    confidences = []
    results = []

    image = cv2_imread(region_path)
    (H, W) = image.shape[:2]

    # determine only the *output* layer names that we need from YOLO
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    blob = dnn.blobFromImage(image, 1 / 255.0, (WIDTH, HEIGHT), swapRB=True, crop=False)

    net.setInput(blob)
    start = time()
    layeroutputs = net.forward(ln)
    end = time()

    # loop over each of the layer outputs
    for output in layeroutputs:

        # loop over each of the detections
        for detection in output:

            # extract the class ID and confidence (i.e., probability) of
            # the current object detection
            scores = detection[5:]
            class_id = np_argmax(scores)
            confidence = scores[class_id]

            # filter out weak predictions by ensuring the detected
            # probability is greater than the minimum probability
            if confidence > CONFIDENCE_THRESHOLD:

                # scale the bounding box coordinates back relative to the
                # size of the image, keeping in mind that YOLO actually
                # returns the center (x, y)-coordinates of the bounding
                # box followed by the boxes' width and height
                box = detection[0:4] * np_array([W, H, W, H])
                (center_x, center_y, width, height) = box.astype("int")

                # use the center (x, y)-coordinates to derive the top and
                # and left corner of the bounding box
                x = int(center_x - (width / 2))
                y = int(center_y - (height / 2))

                # update our list of bounding box coordinates, confidences,
                # and class IDs
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                # classIDs.append(classID)

    # apply non-maxima suppression to suppress weak, overlapping bounding
    # boxes
    idxs = dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, 0.2)

    # ensure at least one detection exists
    if len(idxs) > 0:

        # loop over the indexes we are keeping
        for i in idxs.flatten():

            # extract the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])

            # Array format is: x1, y1, x2, y2
            results.append([x, y, x + w, y + h])

    return results, end - start
