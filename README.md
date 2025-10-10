# 🚀 Full Stack Dockerized Application "# Edge-Monitor" 

This repository contains a **Dockerized Full-Stack Application** with the following tech stack:

- **Frontend**: Angular  
- **Backend**: Spring Boot  
- **API Gateway**: Spring Cloud Gateway
- **Mailing Micro-Service**: Spring Boot 
- **Database**: MySQL  
- **Caching**: Redis  
- **Queueing**: Kafka  
- **Deployment**: AWS EC2 instance
---



## 🧱 Architecture Overview

[ Angular App ] --> [ Spring Cloud Gateway ] --> [ Spring Boot Services ]
| [ MySQL | Redis ]


Each component is containerized using Docker and orchestrated via Docker Compose for local development and deployment on an AWS EC2 instance.

---

## 📦 Tech Stack

| Layer                  | Technology                                             |
|------------------------|--------------------------------------------------------|
| Frontend               | Angular                                                |
| Backend                | Spring Boot                                            |
| API Gateway            | Spring Cloud Gateway                                   |
| Mailing Micro-Service  | Spring Boot                                            |
| Database               | MySQL                                                  |
| Caching                | Redis                                                  |
| Notification Queue     | Kafka                                                  |
| Deployment             | Docker, Docker Compose                                 |
| CICD                   | Git Actions                                            |
| AWS Services           | AWS EC2                                                |

---


## 🛠️ Prerequisites
- Docker & Docker Compose installed
- Open ports: `8080`, `8082`, `8083`, `4200`, `8000`
---


## 🚀 Getting Started (Installation and run instructions)
### 1. Clone the Repository

```bash
git clone https://github.com/bejoyjose1993/HardwareMonitoring.git
cd HardwareMonitoring
```


### 2. Create Enviornment Files (.env.local)
```bash
# .env — Deployment config
# API URL
BASE_API_URL=http://localhost:8082

# MySQL
DB_URL=jdbc:mysql://host.docker.internal:3306/your_db_name
DB_USERNAME=your_db_user_name
DB_PASSWORD=your_db_password
DB_DATABASE=your_db_name
DB_PORT=3306

# Redis
REDIS_HOST=host: host.docker.internal
REDIS_PORT=6379

# Zookeeper
ZOOKEEPER_PORT=2181

# Kafka
KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092
KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092
KAFKA_PORT=9092

# Backend
BACKEND_PORT=8080

# Gateway
GATEWAY_PORT=8082
GATEWAY_SERVICE_URI=http://host.docker.internal:8080
APP_CORS_ALLOWED_ORIGINS=http://localhost:4200

# Frontend
FRONTEND_PORT=4200

# Mailing (Notifiucation Service)
NOTIFICATION_PORT=8083
MAIL_USERNAME=your_own_emailId
MAIL_PASSWORD=your_own_generated_password_to_access_email_client
KAFKA_BOOTSTRAP_SERVER=kafka:9092

# Docker image tags (optional for versioning)
IMAGE_TAG=latest

# EDGE MONITOR
EDGE_MONITOR_PORT=8000
EDGE_MONITOR_TRANSPORT=http
EDGE_MONITOR_ENDPOINT=http://edge_monitor:8000/ingest
EDGE_MONITOR_INTERVAL=5
```

### 3. Build and Run with Docker Compose

```bash
docker-compose --env-file .env.local up --build
```

### 4. Access the Application

Frontend (Angular): http://localhost:4200

API Gateway: http://localhost:8082

MySQL: port 3306

Redis: port 6379

## 🚀 User Interface

### 1. Login Page

![Login Page](User%20Interface%20Images/Edge-Monitor%20LogIn%20Page.png)

### 2. SignIn Page

![SignUp Page](User%20Interface%20Images/Edge-Monitor%20SignUp%20Page.png)

### 3. Dashboard Page

![Dashboard Page](User%20Interface%20Images/Edge-Monitor%20Dashboard%20Page.png)
