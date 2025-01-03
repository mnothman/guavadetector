Requires Python (recommended to use virtual environment e.g., venv / virtualenv)

Download dataset from: https://www.kaggle.com/datasets/asadullahgalib/guava-disease-dataset


Setup Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
 
pip install -r requirements.txt

start flask app:
cd app
python app.py


guava-disease-detector/
│
├── app/
│   ├── app.py                 # Main Flask application
    ├── static/
│   └── templates/             # HTML templates for the web interface
│       └── upload.html        # Defines the structure and design of the web interface
│
├── static/                # Directory for uploaded files
│
├── templates/
│   └── upload.html        # HTML template for the web app
│
├── data/insert dataset here
│
├── model/
│   └──guava_disease_detector.keras
├── requirements.txt       # Python dependencies
└── README.md              # Instructions and project details


Citation

Actual dataset from Mendeley Data:
Amin, Md Al; Mahmud, Md Iqbal; Rahman, Asadullah Bin; Parvin, Mst Aktarina; Mamun, Md Abdulla Al (2024), “Guava Fruit Disease Dataset”, Mendeley Data, V1, doi: 10.17632/bkdkc4n835.1

https://www.kaggle.com/datasets/asadullahgalib/guava-disease-dataset
