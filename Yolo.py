from ultralytics import YOLO
import cv2

def detect_image(image_path):
    model = YOLO('/Users/austinshen/Documents/Umich/MHack/Web/best.pt')

    # Load Image
    image_path = image_path
    img = cv2.imread(image_path)

    #Segmentation
    results = model(img)

    #Returns results as list
    result = results[0]

    #Detect word
    detected_boxes = result.boxes.xyxy  # Bounding boxes in (x1, y1, x2, y2) format
    detected_classes = result.boxes.cls  # Class labels
    detected_scores = result.boxes.conf  # Confidence scores
    detected_masks = result.masks  # Segmentation masks

    ingredient = ""

    # Print detected objects' information
    for i in range(len(detected_boxes)):
        ingredient+= (model.names[int(detected_classes[i])])
        ingredient+= " "
    
    return ingredient

# print (detect_image("/Users/austinshen/Documents/Umich/MHack/Web/static/uploads/Fridge2.jpeg"))