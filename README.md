

---

# Simple Web App – DevOps Portfolio Project

A **production-ready FastAPI microservice** built to demonstrate core **DevOps practices** such as containerization, CI/CD pipelines, and automated testing.

This project is intentionally simple in functionality but strong in **engineering discipline**, making it ideal for **DevOps / Cloud / Platform Engineer portfolios**.

---

## ✨ Features

* ⚡ FastAPI-based microservice
* 🐳 Dockerized application
* 🧪 Automated tests with Pytest
* 🔁 CI pipeline using GitHub Actions
* 🧱 Jenkins pipeline for CI/CD practice
* 🩺 Health check endpoint (load balancer ready)
* 📄 Clean, scalable project structure

---

## 📁 Project Structure

```
simple-web-app/
├── app/
│   ├── __init__.py
│   └── main.py            # FastAPI application
├── tests/
│   ├── __init__.py
│   └── test_health.py     # Health endpoint tests
├── .github/
│   └── workflows/
│       └── ci.yaml        # GitHub Actions CI pipeline
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container configuration
├── .dockerignore          # Docker build exclusions
├── Jenkinsfile            # Jenkins CI/CD pipeline
└── README.md
```

---

## 🚀 Getting Started

### 🔧 Local Development

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start the application:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Open API documentation:

   ```
   http://localhost:8000/docs
   ```

---

## 🧪 Running Tests

```bash
pytest
```

All tests are executed automatically in the CI pipeline.

---

## 🐳 Docker

### Build the Image

```bash
docker build -t simple-web-app .
```

### Run the Container

```bash
docker run -p 8000:8000 simple-web-app
```

Visit:

```
http://localhost:8000
```

---

## 📡 API Endpoints

| Endpoint  | Method | Description                        |
| --------- | ------ | ---------------------------------- |
| `/`       | GET    | Welcome message                    |
| `/health` | GET    | Health check (for monitoring / LB) |

---

## 🔁 CI/CD

### GitHub Actions

* Runs on every push and pull request
* Installs dependencies
* Executes tests automatically

### Jenkins

* Declarative pipeline via `Jenkinsfile`
* Designed for local or self-hosted Jenkins setups
* Demonstrates real-world CI/CD workflow

---

## 🎯 Why This Project?

This project showcases:

* Real DevOps workflows (not just theory)
* CI/CD pipeline implementation
* Container-first development
* Clean, testable application design

It serves as a **foundation** for future improvements such as:

* Kubernetes deployment
* Terraform infrastructure
* Monitoring with Prometheus/Grafana
* Cloud deployment (GCP / AWS / Azure)

---

## 📌 Tech Stack

* **Backend:** FastAPI (Python)
* **Testing:** Pytest
* **CI/CD:** GitHub Actions, Jenkins
* **Containerization:** Docker

---

## 📄 License

This project is open-source and available for educational and portfolio use.

---


