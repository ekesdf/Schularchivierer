import numpy as np
import time
import cv2



CONFIG_FILE  = "ai/char_localization/trained_model/detect_v2.cfg"
WEIGHTS_FILE = "ai/char_localization/trained_model/detect_v2.weights"
CONFIDENCE_THRESHOLD = 0.0
WIDTH = 832
HEIGHT = 832

net = cv2.dnn.readNetFromDarknet(CONFIG_FILE, WEIGHTS_FILE)

def make_char_detection(image_path):


	# initialize our lists of detected bounding boxes, confidences, and
	# class IDs, respectively
	boxes = []
	confidences = []
	results = []
	

	image = cv2.imread(image_path)
	(H, W) = image.shape[:2]

	# determine only the *output* layer names that we need from YOLO
	ln = net.getLayerNames()
	ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]


	blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (WIDTH, HEIGHT),swapRB=True, crop=False)

	net.setInput(blob)
	start = time.time()
	layerOutputs = net.forward(ln)
	end = time.time()


	# loop over each of the layer outputs
	for output in layerOutputs:
		
		# loop over each of the detections
		for detection in output:

			# extract the class ID and confidence (i.e., probability) of
			# the current object detection
			scores = detection[5:]
			classID = np.argmax(scores)
			confidence = scores[classID]

			# filter out weak predictions by ensuring the detected
			# probability is greater than the minimum probability
			if confidence > CONFIDENCE_THRESHOLD:

				# scale the bounding box coordinates back relative to the
				# size of the image, keeping in mind that YOLO actually
				# returns the center (x, y)-coordinates of the bounding
				# box followed by the boxes' width and height
				box = detection[0:4] * np.array([W, H, W, H])
				(centerX, centerY, width, height) = box.astype("int")

				# use the center (x, y)-coordinates to derive the top and
				# and left corner of the bounding box
				x = int(centerX - (width / 2))
				y = int(centerY - (height / 2))

				# update our list of bounding box coordinates, confidences,
				# and class IDs
				boxes.append([x, y, int(width), int(height)])
				confidences.append(float(confidence))
				# classIDs.append(classID)

	# apply non-maxima suppression to suppress weak, overlapping bounding
	# boxes
	idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD,0.35)
	

	# ensure at least one detection exists
	if len(idxs) > 0:
		
		# loop over the indexes we are keeping
		for i in idxs.flatten():
			
			# extract the bounding box coordinates
			(x, y) = (boxes[i][0], boxes[i][1])
			(w, h) = (boxes[i][2], boxes[i][3])

			# Array format is: x1, y1, x2, y2
			results.append([x, y,x+w,y+h])
			cv2.rectangle(image, (x, y), (x + w, y + h), (255,255,0), 2)


	cv2.imwrite("temp/test.jpg", image)

	return results,end-start