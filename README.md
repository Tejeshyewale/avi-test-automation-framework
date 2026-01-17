# 🚀 Avi Load Balancer – Python Test Automation Framework

## 📌 Overview

This repository contains a **Python-based modular test automation framework** designed to interact with a **mock VMware Avi Load Balancer REST API**.
The framework demonstrates **configuration-driven automation**, **authenticated API interaction**, **parallel execution**, and a **structured test lifecycle**.

This project was built as part of a technical assignment to showcase automation design, clean architecture, and real-world debugging skills.

---

## ✨ Key Features

* Python-based automation framework
* YAML-driven configuration (no hardcoded values)
* Token-based authentication using REST APIs
* Parallel execution of test cases
* Modular test workflow:

  * Pre-Fetch
  * Pre-Validation
  * Task / Trigger
  * Post-Validation
* Mock SSH and RDP modules
* Clean and extensible project structure

---

## 🧱 Project Structure

```
avi_test_framework/
├── config/
│   ├── api_config.yaml
│   ├── credentials.yaml
│   └── test_cases.yaml
│
├── core/
│   ├── api_client.py
│   ├── auth.py
│   └── yaml_loader.py
│
├── modules/
│   ├── ssh.py
│   └── rdp.py
│
├── tests/
│   ├── pre_fetcher.py
│   ├── pre_validation.py
│   ├── task_trigger.py
│   └── post_validation.py
│
├── runner.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Configuration

### 🔹 API Configuration (`config/api_config.yaml`)

```yaml
base_url: "https://semantic-brandea-banao-dc049ed0.koyeb.app"
endpoints:
  tenants: "/api/tenant"
  virtual_services: "/api/virtualservice"
  service_engines: "/api/serviceengine"
```

### 🔹 Credentials (`config/credentials.yaml`)

```yaml
username: "your_username"
password: "your_password"
```

> ⚠️ Do not commit real credentials to GitHub. Use placeholders or add this file to `.gitignore`.

### 🔹 Test Cases (`config/test_cases.yaml`)

```yaml
test_cases:
  - name: "Disable Backend VS"
    target_vs_name: "backend-vs-t1r_1000-1"
```

---

## 🔄 Test Execution Workflow

### 1️⃣ Pre-Fetch

* Fetches all tenants, virtual services, and service engines
* Logs the count of each resource

### 2️⃣ Pre-Validation

* Identifies the target Virtual Service by name
* Validates that the Virtual Service is enabled

### 3️⃣ Task / Trigger

* Sends a PUT request to disable the Virtual Service

### 4️⃣ Post-Validation

* Verifies that the Virtual Service is successfully disabled

---

## 🧪 Mock Components

* **SSH Module:** Simulates SSH connectivity
* **RDP Module:** Simulates remote desktop validation

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Register a user (one-time)

```http
POST https://semantic-brandea-banao-dc049ed0.koyeb.app/register
```

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### 3️⃣ Execute the framework

```bash
python runner.py
```

---

## ✅ Sample Output

```
Runner started...
Login successful
Tenants: 1
Virtual Services: 25
Service Engines: 25
Found target VS: backend-vs-t1r_1000-1
Pre-validation passed
Disabling Virtual Service...
Virtual Service disabled
Post-validation successful
Runner finished.
```

---

## 🛠 Technologies Used

* Python 3
* REST APIs
* YAML
* requests
* concurrent.futures

---

## 🎯 Learning Outcomes

* Designed a scalable test automation framework
* Worked with authenticated REST APIs
* Implemented parallel execution
* Practiced real-world debugging and API response handling
* Followed clean, modular Python architecture

---

## ℹ️ Notes

* Uses a mock API environment
* No real infrastructure is modified
* Built for learning, assessment, and interview demonstration

---

## 👤 Author

**Tejesh Yewale**
Computer Engineering Student | Data Science & Cloud Enthusiast
