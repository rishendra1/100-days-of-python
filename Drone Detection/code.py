from ultralytics import YOLO

# Load a model
model = YOLO("Drones.pt")  # pretrained YOLO11n model

# Run batched inference on a list of images
results = model(["Sample1.jpg"])  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    result.show()         # display to screen
    result.save(filename="result.jpg")  # save to disk
