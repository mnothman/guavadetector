Model that detects health of a guava based on user uploaded image <br/>
Citation of dataset below <br/> <br/>

![HomepageGuava](https://github.com/user-attachments/assets/357175e6-9ed0-454a-b9e3-b9b0e2868e2c)

 <br/> <br/>

![diseasedGuava](https://github.com/user-attachments/assets/46a0a6a9-c7d4-42e6-8ee0-1b3a25d0b8c7)

 <br/> <br/>

Requires Python (recommended to use virtual environment e.g., venv / virtualenv) <br/> <br/>

### 1. Clone Repository <br/> <br/>

git clone https://github.com/mnothman/guavadetector.git <br/>


### 2. Setup Environment (optional) <br/>
python -m venv venv <br/>
source venv/bin/activate  # On Windows: venv\Scripts\activate <br/><br/>

pip install -r requirements.txt <br/><br/>

### 3. Download Dataset <br/><br/>

Download dataset from: https://www.kaggle.com/datasets/asadullahgalib/guava-disease-dataset <br/><br/>

Extract to: /data/ <br/>
Full default path should be: /data/archive/GuavaDiseaseDataset <br/>
Can modify base directory of data in train.py: "BASE_DIR = /data/archive/GuavaDiseaseDataset" <br/> <br/>

### 4. Train Model <br/>
cd model <br/>
python train.py <br/><br/>

wait for guava_disease_detector.keras to finish training <br/><br/>

model/ <br/>
└── guava_disease_detector.keras <br/> <br/>

### 5. Run the Flask App <br/><br/>

start flask app: <br/>
cd app <br/>
python app.py <br/><br/>

Open browser at http://localhost:5000/ <br/><br/><br/>



guava-disease-detector/ <br/>
│ <br/>
├── app/ <br/>
│   ├── app.py                       # Main Flask application <br/>
│   ├── static/ <br/>
│   └── templates/ <br/>
│       └── upload.html <br/>
│ <br/>
│ <br/>
├── data/archive/GuavaDiseaseDataset/ <br/>
│                                ├── test/ <br/>
│                                ├── train/ <br/>
│                                └── val/  <br/>
│ <br/>
├── model/ <br/>
│   ├── guava_disease_detector.keras # Trained Model <br/>
│   ├── preprocess.py <br/>
│   └── train.py <br/><br/><br/>


Citation <br/>

Actual dataset from Mendeley Data: <br/>
Amin, Md Al; Mahmud, Md Iqbal; Rahman, Asadullah Bin; Parvin, Mst Aktarina; Mamun, Md Abdulla Al (2024), “Guava Fruit Disease Dataset”, Mendeley Data, V1, doi: 10.17632/bkdkc4n835.1 <br/><br/>

https://www.kaggle.com/datasets/asadullahgalib/guava-disease-dataset <br/>
