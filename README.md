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


## 🚀 Getting Started
### 1. Clone the Repository

```bash
git clone https://github.com/bejoyjose1993/HardwareMonitoring.git
cd HardwareMonitoring
```
