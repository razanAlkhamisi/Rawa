# Rawa

# 🌿 Smart Irrigation System Using Artificial Intelligence

## 🚀 Overview

Rawa is an AI-powered, IoT-enabled Django platform designed to revolutionize modern agriculture. Instead of traditional fixed-schedule watering, Rawa "listens" to the soil using smart sensors and "sees" the plants through Computer Vision.

By integrating Machine Learning, IoT sensors, and a Raspberry Pi controller, the system delivers real-time monitoring, precise watering decisions, and acts as a digital doctor by detecting early signs of plant disease—all managed through a single, intuitive web dashboard. It’s about saving water, saving time, and growing healthier crops through a data-driven approach.

---

## 💡 Key Features

* 🌱 **Automated Irrigation Control**

  * Uses ML models to analyze soil-moisture, temperature, and humidity data.
  * Activates irrigation **only when needed**, preventing overwatering and saving water.

* 🔍 **Plant Identification & Disease Detection**

  * Employs computer-vision models to recognize plant species and detect early disease symptoms.
  * Supports timely action and personalized watering per plant type.

* 🌐 **IoT & Raspberry Pi Integration**

  * **Sensors:** Soil-moisture, DHT11/DHT22 (temperature & humidity), light-intensity, etc.
  * **Raspberry Pi:** Collects data, controls pumps/valves, and sends information to the Django backend through Wi-Fi or MQTT.

* 💻 **Web Dashboard (Django)**

  * Displays live sensor readings and irrigation status.
  * Allows manual or automatic irrigation control.
  * Shows AI insights, disease alerts.

---

## ⚙️ Tech Stack

| Layer             | Technologies Used                                                         |
| ----------------- | ------------------------------------------------------------------------- |
| **Hardware**      | Raspberry Pi 4 / 3B+, Soil Moisture Sensor, DHT11/DHT22, Water Pump Relay |
| **Backend**       | Django, Python, REST API                                                  |
| **Frontend**      | HTML, CSS, JavaScript (or React)                                          |
| **AI Models**     | ML for irrigation prediction, CV for plant & disease detection            |

---

### Dashboard Preview

<img width="589" height="550" alt="dash" src="https://github.com/user-attachments/assets/c8ba7355-ce6f-42d6-b2c6-0e42047f2d9c" />


---

## 🖼️ Computer Vision Demo

The AI-powered computer vision module analyzes uploaded leaf images to:

- 🌿 Identify the plant species.
- 🔍 Detect whether the plant is healthy or diseased.
- ⚠️ Classify the detected disease (when applicable).

### 🌱 Healthy Plant

<img width="587" height="549" alt="safe" src="https://github.com/user-attachments/assets/fd6d092e-e346-4ebb-8d95-03e482a3a0b1" />


---

### 🍂 Diseased Plant

<img width="587" height="549" alt="affected" src="https://github.com/user-attachments/assets/7a31f080-2f65-479b-8eb9-95536e98f347" />




---

## 🧩 System Architecture

```
[ IoT Sensors ]
       ↓
[ Raspberry Pi ]  → Sends data to Django Backend
       ↓
[ ML/CV Models ] → Analyze data & generate decisions
       ↓
[ Django Server ] → Controls pump + shows dashboard
       ↓
[ Web Dashboard / User Interface ]
```

<img width="656" height="406" alt="11" src="https://github.com/user-attachments/assets/5423bf5a-b7ce-4dc6-a4f5-4bc07fd5bd07" />


---
## 🌾 Benefits

* 💧 Smart water management for sustainability
* 🌿 Data-driven decisions for healthier plants
* ⚡ Real-time IoT monitoring & control
* ♻️ Environmentally friendly agriculture

---

## 🔮 Future Enhancements

* Weather-forecast API integration
* Web application for remote monitoring
* Machine learning for adaptive irrigation schedules
* Computer vision for detecting plant type, identifying diseases, and classifying their kind


---

## 🎯 Project Vision

To empower sustainable agriculture through **AI and IoT**, providing farmers with intelligent, automated, and accessible tools that make irrigation smarter, faster, and more efficient.
