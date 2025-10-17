# 🧠 YOLOv8 Object Detection API (Flask)

A simple object detection pipeline using **YOLOv8** exposed via a **Flask API**.  
The model detects objects (e.g., “chair”) in uploaded images or test images from a folder.

---

## 🚀 Features
- Uses pretrained **YOLOv8n.pt** model  
- Detects one object class (default: **chair**)  
- Runs inference on images in `test_data/`  
- Saves annotated results to `results/`  
- Flask endpoint `/detect` accepts image uploads and returns JSON output

---

## 📁 Folder Structure

yolov8_flask/
├── app.py                     # Flask API exposing /detect endpoint
├── detect.py                  # YOLOv8 inference logic
├── requirements.txt           # Required Python packages
├── README.md                  # Documentation (project overview)
└── data_files/
    ├── test_images/           # Input test images (e.g., chair1.jpg, chair2.jpg)
    └── results/               # Output images with bounding boxes & labels

