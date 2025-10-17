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
object_detection/
├── app.py
├── detect.py
├── requirements.txt
├── data_files/
│   ├── test_images/
│   └── results/

