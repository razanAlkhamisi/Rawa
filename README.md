# Rawa
#Rawa Project

# 🌿 Smart Irrigation System Using Artificial Intelligence

## 🚀 Overview

**Smart Irrigation System** is an **AI-powered, IoT-enabled Django web platform** designed to automate and optimize irrigation.
By integrating **Machine Learning**, **Computer Vision**, **IoT sensors**, and a **Raspberry Pi controller**, the system delivers real-time monitoring, precise watering decisions, and early disease detection — all from a single web dashboard.

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
