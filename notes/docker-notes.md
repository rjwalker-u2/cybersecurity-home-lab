# Docker Notes

These are my personal notes while learning how to build and run containers, create images, and deploy multi-service applications for security tools.

---

## 🐳 Why I Use Docker
- Makes security tools portable  
- Easy to spin up and shut down environments  
- Great for building scanners, APIs, log tools, and testing environments  
- Works perfectly for multi-container projects

---

## 🧱 Key Docker Concepts

### **1. Containers vs Images**
- **Image** = blueprint (like a class)
- **Container** = running instance (like an object)

### **2. Dockerfile**
A file that defines how your image is built.

Common instructions:
- `FROM` — base image  
- `COPY` — move files into image  
- `RUN` — install packages, set up environment  
- `CMD` — default command  
- `EXPOSE` — ports the container listens on  

---

## 🏗️ Multi-Stage Dockerfile
Helps make images smaller and more secure.

Example stages:
- **Builder stage** → install packages, build tools  
- **Final stage** → copy only the final app  

This reduces image size and cuts out unnecessary files.

---

## 🔐 Running as a Non-Root User
A best practice for security:
- Add user  
- Switch to that user  
- Prevents containers from running with unnecessary privileges  

---

## 🧩 Docker Compose
Lets you run multiple containers at once (like your scanner + log analyzer).

Key features:
- Networking  
- Volumes  
- Environment variables  
- Healthchecks  

Example:
- API container  
- Log analyser container  
- Both networked together  

---

## ❤️ Healthchecks
Used to monitor whether a container is functioning.

Example:
```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
  interval: 30s
  timeout: 10s
  retries: 3
