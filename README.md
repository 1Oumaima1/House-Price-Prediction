Here is your cleaned and well-organized `README.md` without emojis and with improved structure:

---

# House Price Prediction App

This project is a machine learning application that predict house prices based on the Ames Housing dataset. This project demonstrates a production-ready pipeline: from raw data cleaning to deployment via a FastAPI backend and an interactive Streamlit dashboard, all containerized with Docker.

---

## Project Structure

```text
House_Price_Prediction/
│
├── data/                      # Dataset files
│   ├── train.csv              # Training data
│   ├── test.csv               # Test data
│   ├── data_description.txt   # Detailed feature descriptions
│   └── submission.csv         # Sample submission file
│
├── src/                       # ML Pipeline Source Code
│   ├── data_preprocessing.py  # Cleaning and encoding logic
│   ├── train_model.py         # Scikit-learn pipeline construction
│   ├── predict.py             # Inference functions
│   └── house_model.pkl        # Saved serialized model
│
├── notebook/                  # EDA & Experimentation
│   └── exploration.ipynb
│
├── main.py                    # Training entry point
├── app.py                     # REST API (FastAPI)
├── dashboard.py               # Interactive UI (Streamlit)
│
├── Dockerfile                 # Containerization setup
├── .dockerignore              # Files excluded from Docker
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Objectives

The goal of this project is to predict house prices using features like living area, overall quality, and year built, then deploy the model through:

* REST API (FastAPI): For programmatic access and integration
* Interactive Dashboard (Streamlit): For user-friendly predictions and visualizations

---

## Getting Started

### 1. Local Setup

#### Create Virtual Environment

```bash
python -m venv .venv
```

#### Activate Environment

* Windows:

```bash
.venv\Scripts\activate
```

* Linux / Mac:

```bash
source .venv/bin/activate
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Training the Model

Run the main pipeline to clean data, train the model, and save the `.pkl` file:

```bash
python main.py
```

---

## Docker Deployment

The project is fully containerized.

To avoid common DNS resolution issues during the build process (especially on Windows/WSL2), explicit host mapping is used.

### Build the Image

```bash
docker build --add-host pypi.org:151.101.0.223 --add-host files.pythonhosted.org:151.101.128.223 -t house-price-app .
```

### Run the Container

```bash
docker run -p 8501:8501 house-price-app
```

Access the dashboard at:
[http://localhost:8501](http://localhost:8501)

---

## Machine Learning Pipeline

The model utilizes a Scikit-learn Pipeline consisting of:

* Imputation: Handling missing values using SimpleImputer (median strategy)
* Scaling: Feature normalization using StandardScaler
* Regressor: RandomForestRegressor with 100 estimators

---

## Features and Data

Key features used for prediction:

* GrLivArea: Above grade (ground) living area square feet
* OverallQual: Overall material and finish quality (1–10)
* YearBuilt: Original construction date
* TotalBsmtSF: Total square feet of basement area

---

## Technical Stack

| Tool / Library | Usage                           |
| -------------- | ------------------------------- |
| Python         | Core Programming                |
| Pandas         | Data Manipulation               |
| Scikit-learn   | ML Modeling and Pipelines       |
| FastAPI        | Backend REST API                |
| Streamlit      | Frontend UI/UX                  |
| Docker         | Containerization and Deployment |

---

