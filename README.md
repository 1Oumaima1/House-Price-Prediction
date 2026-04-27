# House Price Prediction App

This project is a machine learning application that predicts house prices based on various features. It features a **FastAPI** backend and a **Streamlit** frontend, all containerized using **Docker**.

##  Technologies Used
* **Python** (Pandas, Scikit-learn, Joblib)
* **FastAPI** (Backend API)
* **Streamlit** (Frontend Dashboard)
* **Docker** (Containerization)

##  How to Run with Docker

To avoid DNS resolution issues (especially on WSL2/Windows), build the image using the following command:

```bash
docker build --add-host pypi.org:151.101.0.223 --add-host files.pythonhosted.org:151.101.128.223 -t house-price-app .