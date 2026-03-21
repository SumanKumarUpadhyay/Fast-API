# ⚡ FastAPI Mastery - Complete Learning Repository

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat&logo=pydantic)](https://docs.pydantic.dev/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker)](https://docker.com)
[![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazon-aws)](https://aws.amazon.com)

> **Complete FastAPI journey from basics to production deployment** - Following CampusX Course

---

## 📚 What I Learned

### 🔹 FastAPI Basics
REST APIs, path/query parameters, HTTP methods, async endpoints, automatic Swagger/ReDoc documentation, dependency injection

### 🔹 Pydantic Validation
Data validation with BaseModel, custom validators, nested models, type checking, request/response serialization

### 🔹 ML Model Integration
Loading ML models (scikit-learn), prediction endpoints, data preprocessing, batch predictions, model versioning

### 🔹 Docker Containerization
Dockerfile optimization, multi-stage builds, docker-compose for multi-container apps, environment configuration

### 🔹 AWS Deployment
- **EC2** - Virtual machine deployment with uvicorn
- **ECS** - Container orchestration with ECR + Fargate  
- **Lambda** - Serverless deployment using Mangum adapter

---

## 📂 Repository Structure
Fast-API/
├── main.py # Main FastAPI app (Insurance Premium)
├── patients.json # Sample patient data
├── Pydantic/ # Pydantic model examples
├── Dockerfile # Container configuration
└── requirements.txt # Dependencies


---

## 🚀 Quick Start

```bash
git clone https://github.com/SumanKumarUpadhyay/Fast-API.git
cd Fast-API
pip install fastapi uvicorn pydantic
uvicorn main:app --reload

API Docs: http://localhost:8000/docs

🎯 Project: Insurance Premium Prediction
A complete ML API that predicts insurance premiums based on patient health parameters with:

✅ Pydantic request validation
✅ Trained ML model (Random Forest)
✅ Error handling & custom exceptions
✅ JSON data storage
✅ Auto-generated API documentation

🐳 Docker Deployment
bash
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
docker-compose up
☁️ AWS Deployment Options
Service	Method
EC2	SSH → Clone repo → Run uvicorn
ECS	Push to ECR → Create task → Fargate
Lambda	Mangum adapter → API Gateway
🔗 Course Reference
FastAPI for Machine Learning - CampusX Playlist

👨‍💻 Author
Suman Kumar Upadhyay
GitHub

⭐ Star this repo if you found it helpful!
