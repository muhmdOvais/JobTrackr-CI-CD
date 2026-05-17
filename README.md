# 🚀 JobTrackr – Full Stack Django DevOps Project

A fully containerized Django Job Tracking web application deployed using a real-world CI/CD pipeline with Jenkins Master-Agent architecture on AWS EC2.

---

# 🌐 Live Architecture

```text
Developer Pushes Code to GitHub
            ↓
GitHub Webhook Triggers Jenkins
            ↓
Jenkins Master (Local Ubuntu)
            ↓
Jenkins Agent/Slave (AWS EC2)
            ↓
Docker Image Build
            ↓
Container Deployment on EC2
            ↓
Live Django Website Updated Automatically
```

---

# 📸 Screenshots To Add

## 🔹 Application Screenshots

Take screenshots of:

1. Login Page
2. Register Page
3. Dashboard Page
4. Add Job Page
5. Job Entries Table

---

## 🔹 DevOps Screenshots

Take screenshots of:

1. Successful Jenkins Pipeline
2. Jenkins Node Online Status
3. GitHub Webhook Deliveries (200 OK)
4. Docker Containers Running (`docker ps`)
5. Website Running on EC2 Public IP
6. Jenkins Pipeline Stages
---

# 📌 Project Overview

JobTrackr is a Django-based web application that helps users:

* Register/Login securely
* Track job applications
* Add/Edit/Delete job entries
* Monitor application status
* Store application notes
* Manage personal job dashboard

The project was later transformed into a complete DevOps CI/CD project using:

* Docker
* Docker Compose
* Jenkins Pipelines
* Jenkins Master-Agent Architecture
* GitHub Webhooks
* AWS EC2

---

# 🛠️ Technologies Used

## 🔹 Backend

* Python 3.12
* Django 6
* SQLite3

## 🔹 DevOps & Deployment

* Docker
* Docker Compose
* Jenkins
* GitHub Webhooks
* AWS EC2
* Git
* GitHub
* Ngrok

## 🔹 Infrastructure

* Jenkins Master on Local Ubuntu Machine
* Jenkins Agent/Slave on AWS EC2

---

# ✨ Features

✅ User Authentication

* User Registration
* User Login
* User Logout

✅ Job Management

* Add Job Applications
* Edit Job Entries
* Delete Job Entries
* Track Application Status

✅ Dashboard

* Total Applications
* Interviews Count
* Offers Count
* Rejected Count

✅ DevOps Features

* Dockerized Application
* Automated CI/CD Pipeline
* Automatic Deployment on GitHub Push
* Jenkins Distributed Build Architecture
* Webhook Integration

---

# 📂 Project Structure

```bash
JobTrackr/
│
├── tracker/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── jobtrackr/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── requirements.txt
├── manage.py
└── README.md
```

---

# 🐳 Docker Setup

## Dockerfile

The application is fully containerized using Docker.

### Docker Build

```bash
docker build -t jobtrackr-app .
```

### Run Container

```bash
docker run -d -p 8000:8000 --name jobtrackr-container jobtrackr-app
```

---

# ⚙️ Docker Compose Setup

The application deployment is managed using Docker Compose.

### Start Application

```bash
docker compose up -d --build
```

### Stop Application

```bash
docker compose down
```

---

# 🔧 Jenkins CI/CD Pipeline

## Jenkins Architecture

### 🖥️ Jenkins Master

* Runs on Local Ubuntu Machine
* Handles:

  * Webhooks
  * Pipeline Management
  * Job Scheduling
  * Build Triggering

### ☁️ Jenkins Agent/Slave

* Runs on AWS EC2
* Handles:

  * Docker Builds
  * Container Deployment
  * Pipeline Execution

---

# 🔁 CI/CD Workflow

```text
Code Push to GitHub
        ↓
GitHub Webhook Trigger
        ↓
Jenkins Pipeline Starts
        ↓
EC2 Agent Pulls Latest Code
        ↓
Docker Image Builds
        ↓
Old Container Removed
        ↓
New Container Deployed
        ↓
Updated Website Goes Live
```

---

# 📜 Jenkins Pipeline Stages

## 1️⃣ Clone Code

Pull latest code from GitHub repository.

## 2️⃣ Build Docker Image

Build latest application image.

## 3️⃣ Remove Old Container

Remove previous running container.

## 4️⃣ Deploy Updated Container

Run updated Docker container.

---

# 🧠 Key DevOps Concepts Learned

* CI/CD Pipelines
* Jenkins Pipelines
* Jenkins Master-Agent Architecture
* Docker Containerization
* Docker Compose
* GitHub Webhooks
* AWS EC2 Deployment
* SSH Agent Communication
* Automated Deployment
* Container Lifecycle Management
* Django Production Deployment Concepts

---


✅ Jenkins Agent Java Compatibility Issue

Problem:

```text
Jenkins agent disconnecting due to Java version mismatch.
```

Solution:

```bash
sudo apt install openjdk-21-jdk -y
```

---

# 🚀 How to Run Locally

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/JobTrackr.git
cd JobTrackr
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Run Server

```bash
python manage.py runserver
```

---

# ☁️ AWS EC2 Setup

## EC2 Configuration

* Ubuntu Server 24.04 LTS
* t3.small Instance
* Docker Installed
* Docker Compose Installed
* Java 21 Installed
* Jenkins Agent Connected via SSH

---

# 🔗 GitHub Webhook Setup with Ngrok

This project uses **GitHub Webhooks** to automatically trigger the Jenkins CI/CD pipeline whenever new code is pushed to GitHub.

Since Jenkins Master runs locally on Ubuntu, **Ngrok** is used to expose the local Jenkins server to the public internet.

---

# 🚀 Step 1 — Install Ngrok

```bash
snap install ngrok
```

---

# 🚀 Step 2 — Create Ngrok Account

Create a free account:

https://dashboard.ngrok.com/signup

---

# 🚀 Step 3 — Get Ngrok Auth Token

Copy your auth token from:

https://dashboard.ngrok.com/get-started/your-authtoken

---

# 🚀 Step 4 — Configure Ngrok

Run:

```bash
ngrok config add-authtoken YOUR_AUTH_TOKEN
```

Example:

```bash
ngrok config add-authtoken 2asdXxxxxxxxxxxxxxxxx
```

---

# 🚀 Step 5 — Expose Jenkins Port

Jenkins runs locally on:

```text
http://localhost:8080
```

Expose it publicly using:

```bash
ngrok http 8080
```

---

# 🚀 Step 6 — Copy Public URL

Ngrok generates a public URL like:

```text
https://random-name.ngrok-free.app
```

This URL temporarily exposes local Jenkins to GitHub.

---

# 🚀 Step 7 — Configure GitHub Webhook

Navigate to:

```text
GitHub Repository
→ Settings
→ Webhooks
→ Add Webhook
```

---

# 🚀 Step 8 — Add Webhook URL

Payload URL:

```text
https://YOUR_NGROK_URL/github-webhook/
```

Example:

```text
https://abcd-103-21-44-11.ngrok-free.app/github-webhook/
```

---

# 🚀 Step 9 — Webhook Settings

## Content Type

```text
application/json
```

## Events

Choose:

```text
Just the push event
```

---

# 🚀 Step 10 — Save Webhook

Click:

```text
Add Webhook
```

---

# 🚀 Step 11 — Test Webhook

Push any code change:

```bash
git add .
git commit -m "Testing webhook"
git push
```

---

# ✅ Expected Result

After push:

- GitHub sends webhook event
- Jenkins pipeline triggers automatically
- Docker image rebuilds
- Updated container deploys on EC2

# 🧠 Why Ngrok Was Needed

GitHub cannot access:

```text
localhost:8080
```

directly because it is private to the local machine.

Ngrok creates a secure public tunnel:

```text
GitHub → Ngrok URL → Local Jenkins Server
```

allowing GitHub webhooks to trigger Jenkins pipelines automatically.

---

# ☁️ Alternative (Using Jenkins Master on AWS EC2)

If Jenkins Master itself is hosted on an AWS EC2 instance with a public IP address, then Ngrok is NOT required.

You can directly use:

```text
http://YOUR_JENKINS_MASTER_PUBLIC_IP:8080/github-webhook/
```

as the GitHub webhook payload URL.

This is more production-like and avoids dependency on Ngrok tunnels.

---

# 🏆 Project Highlights

✅ Real CI/CD Pipeline

✅ Jenkins Distributed Build Architecture

✅ Dockerized Django Application

✅ Automated Deployment

✅ AWS EC2 Deployment

✅ GitHub Webhook Integration

✅ Real-World DevOps Workflow

---

# 📈 Future Improvements

* Nginx Reverse Proxy
* HTTPS with SSL
* PostgreSQL Integration
* Kubernetes Deployment
* Terraform Infrastructure
* SonarQube Integration
* Prometheus & Grafana Monitoring
* DockerHub Automated Builds

---

# 👨‍💻 Author

## Mohammed Ovais

Computer Science Engineering Student
DevOps & Cloud Enthusiast

---
