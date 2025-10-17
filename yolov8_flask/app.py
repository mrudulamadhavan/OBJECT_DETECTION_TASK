from flask import Flask, render_template, request
import os
import uuid
from detect import detect_objects

app = Flask(__name__)

UPLOAD_FOLDER = 'data_files/test_data'
RESULT_FOLDER = 'data_files/results'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    image_path = None
    output_path = None
    detections = []

    if request.method == 'POST':
        file = request.files['image']
        if file:
            ext = file.filename.rsplit('.', 1)[-1]
            uid = str(uuid.uuid4())
            input_filename = f"{uid}.{ext}"
            output_filename = f"result_{uid}.{ext}"

            input_path = os.path.join(UPLOAD_FOLDER, input_filename)
            output_img_path = os.path.join(RESULT_FOLDER, output_filename)

            file.save(input_path)

            # Detect and get results
            detections = detect_objects(input_path, output_img_path)

            # Paths relative to static/ for HTML rendering
            image_path = f"test_data/{input_filename}"
            output_path = f"results/{output_filename}"

    return render_template('index.html',
                           image_path=image_path,
                           output_path=output_path,
                           detections=detections)

if __name__ == '__main__':
    app.run(debug=True)
