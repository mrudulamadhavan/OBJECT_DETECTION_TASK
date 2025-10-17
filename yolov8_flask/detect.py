from ultralytics import YOLO

# Load model once
model = YOLO("yolov8n.pt")  # You can use yolov8s.pt or yolov8x.pt if you prefer

def detect_objects(input_path, output_path):
    # Run detection
    results = model(input_path)[0]

    # Save output image with boxes
    results.save(filename=output_path)

    # Prepare detection data
    detections = []
    for box in results.boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]
        confidence = float(box.conf[0])
        bbox = box.xyxy[0].tolist()

        detections.append({
            'class': cls_name,
            'confidence': confidence,
            'bbox': [round(coord, 2) for coord in bbox]
        })

    return detections
