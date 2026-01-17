# Avi Load Balancer – Python Test Automation Framework

## Overview
This project is a **Python-based modular test automation framework** built to interact with a **mock VMware Avi Load Balancer REST API**.  
It demonstrates configuration-driven automation, authenticated API handling, parallel execution, and structured test validation.

The focus of this project is **automation design and framework structure**, not real infrastructure management.

---

## Features
- Python-based automation framework
- YAML-driven configuration (no hardcoded values)
- Token-based API authentication
- Parallel test execution
- Modular test stages:
  - Pre-Fetch
  - Pre-Validation
  - Task / Trigger
  - Post-Validation
- Mock SSH and RDP components
- Clean and extensible folder structure

---

## Project Structure

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


---

## Configuration

### API Configuration (`config/api_config.yaml`)
```yaml
base_url: "https://semantic-brandea-banao-dc049ed0.koyeb.app"
endpoints:
  tenants: "/api/tenant"
  virtual_services: "/api/virtualservice"
  service_engines: "/api/serviceengine"

### Test Workflow

Each test case follows these stages:

Pre-Fetch

Fetch tenants, virtual services, and service engines

Log resource counts

Pre-Validation

Identify the target Virtual Service

Validate that it is enabled

Task / Trigger

Disable the Virtual Service using a PUT API call

Post-Validation

Verify that the Virtual Service is disabled
