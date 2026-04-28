# 🚗 Vehicle Insurance Prediction - End-to-End MLOps Project

An end-to-end **Machine Learning + MLOps pipeline** for predicting vehicle insurance outcomes, designed with production-grade practices including **data ingestion, validation, model training, deployment, and CI/CD automation**.

---

## 📌 Project Highlights

* 🔄 Complete ML lifecycle (Data → Model → Deployment)
* ☁️ Cloud integration using AWS (S3, EC2, ECR, IAM)
* 🔗 MongoDB Atlas for scalable data storage
* 🐳 Dockerized application for portability
* ⚙️ CI/CD pipeline using GitHub Actions
* 📊 Modular pipeline architecture (clean, reusable code)
* 🌐 Deployed as a web application

---

## 🧠 Architecture Overview

```
Data Source (MongoDB Atlas)
        ↓
Data Ingestion
        ↓
Data Validation
        ↓
Data Transformation
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Pusher (AWS S3)
        ↓
Prediction Pipeline (Flask App)
        ↓
Deployment (Docker + EC2)
```

---

## 🛠️ Tech Stack

### 💻 Programming & Frameworks

* Python 3.10
* Flask (Web App)
* Scikit-learn
* Pandas, NumPy

### 📦 MLOps & Pipeline

* Modular pipeline design (Custom components)
* Logging & Exception handling
* YAML-based schema validation

### 🗄️ Data Storage

* MongoDB Atlas (Cloud NoSQL DB)

### ☁️ Cloud Services (AWS)

* S3 → Model storage
* EC2 → Deployment server
* ECR → Docker image registry
* IAM → Secure access management

### ⚙️ DevOps & CI/CD

* GitHub Actions (automation)
* Self-hosted runner (EC2)
* Environment variables management

### 🐳 Containerization

* Docker
* DockerHub / AWS ECR

---

## 🔍 Key Features

✔ Automated Data Ingestion from MongoDB
✔ Schema-based Data Validation
✔ Feature Engineering Pipeline
✔ Model Training & Evaluation
✔ Model Versioning in S3
✔ Fully Automated CI/CD Pipeline
✔ Dockerized Deployment
✔ Scalable Cloud Infrastructure

---

## ⚙️ Project Setup

### 1️⃣ Create Environment

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
```

---

### 2️⃣ MongoDB Setup

* Create cluster in MongoDB Atlas
* Add IP: `0.0.0.0/0`
* Get connection string

```bash
export MONGODB_URL="your_mongodb_connection_string"
```

---

### 3️⃣ Run Training Pipeline

```bash
python demo.py
```

---

### 4️⃣ Run Application

```bash
python app.py
```

---

## ☁️ AWS Setup (Core Steps)

* Create IAM user with access keys
* Setup S3 bucket for model storage
* Configure environment variables:

```bash
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
```

---

## 🔄 CI/CD Pipeline

* GitHub Actions triggers on push
* Builds Docker image
* Pushes to AWS ECR
* Deploys on EC2 using self-hosted runner

---

## 🐳 Docker Setup

```bash
docker build -t vehicle-app .
docker run -p 5080:5080 vehicle-app
```

---

## 🌐 Deployment

* Hosted on AWS EC2
* Accessible via:

```
http://<EC2-PUBLIC-IP>:5080
```

---

## 📂 Project Structure

```
src/
 ├── components/
 ├── pipeline/
 ├── entity/
 ├── configuration/
 ├── aws_storage/
 ├── utils/

notebook/
templates/
static/
```

---

## 📈 What Makes This Project Stand Out?

* ✅ Real-world MLOps architecture (not just model training)
* ✅ Cloud-native deployment (AWS)
* ✅ CI/CD automation (industry standard)
* ✅ Scalable and modular design
* ✅ Production-ready practices

---

## 📬 Future Improvements

* Add MLflow for experiment tracking
* Add Kubernetes for scaling
* Add API authentication
* Add monitoring & logging dashboards

---

## 👨‍💻 Author

**Sravan**

---

⭐ If you found this project useful, consider giving it a star!
