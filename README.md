# 🦯 AI-Powered Navigation Device for the Visually Impaired

> A wearable AI assistant enabling fully independent mobility for visually impaired users — combining real-time computer vision, natural-language voice interaction, and solar-powered hardware.

**Team:** JAMBO | Inha University in Tashkent — Creative Engineering & Design Course  
**Status:** ✅ Completed & Graded (Top Grade)

---

## 🎯 Problem Statement

Visually impaired individuals in Uzbekistan face significant barriers to independent mobility, often relying on a human guide for daily navigation. Existing assistive tools (white canes, guide dogs) provide limited situational awareness and no two-way communication.

**Our goal:** Build an affordable, wearable AI navigation assistant that gives visually impaired users full independence — without needing another person.

---

## 💡 Solution Overview

A wearable device that uses a camera to see the environment, processes it with AI, and speaks to the user in real time — while also listening and responding to their questions.

```
Camera → OpenCV (obstacle detection) → TTS Engine → Speaker
                                     ↑
                               Voice Recognition
                               (user speaks back)
```

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎥 **Real-time obstacle detection** | OpenCV-based CV detects obstacles up to **10 meters** |
| 🔊 **Voice-based situational awareness** | Continuous low-latency audio feedback |
| 🗣️ **Two-way conversation** | Natural language interface — user can ask questions |
| ☀️ **Off-grid operation** | Solar charging panel for fully portable, outdoor use |
| 🔬 **User-validated** | Tested with **6 visually impaired users** at Tashkent Library for the Blind |

---

## 🔧 Hardware Components

Designed in **Autodesk Fusion 360**:

- 📷 Camera module
- 🎤 Microphone
- 🔊 Speaker
- ☀️ Solar charging panel
- 🧠 Microcontroller unit (custom PCB design)
- 📡 Sensor array

> CAD files (`.f3d`) for the sensor and microcontroller are included in this repository.

---

## 💻 Software Stack

```
Language:     Python
CV Library:   OpenCV
Speech:       Text-to-Speech (TTS) + Voice Recognition
OS:           Linux (Raspberry Pi / embedded)
Design:       Autodesk Fusion 360 (hardware)
Research:     FigJam (User Research + Ideation)
```

---

## 🔬 User Research

Conducted structured interviews with **6 visually impaired users** at the **Tashkent Library for the Blind**.

Key insights that shaped our design:
- Users needed **voice feedback within 1–2 seconds** — we optimized for low-latency pipeline
- Users wanted to **ask questions freely**, not just receive one-way alerts — led to conversational interface
- **Off-grid portability** was critical for daily outdoor use — led to solar panel integration

> FigJam User Research Board: [View Board](https://www.figma.com/board/qg7lBPsjFeo03SOgxDdStl/User-Reasearch?node-id=0-1)  
> FigJam Ideation Board: [View Board](https://www.figma.com/board/MpUXXWDuAU2LpKEcIu8xjI/Ideation?node-id=0-1)

---

## 📁 Repository Structure

```
📦 ai-navigation-device-visually-impaired
 ┣ 📂 hardware/
 ┃ ┣ 📄 sensor.f3d              # Fusion 360 CAD — sensor unit
 ┃ ┗ 📄 microcontroller.f3d     # Fusion 360 CAD — microcontroller housing
 ┣ 📂 software/
 ┃ ┣ 📄 main.py                 # Main pipeline
 ┃ ┣ 📄 obstacle_detection.py   # OpenCV detection module
 ┃ ┗ 📄 voice_interface.py      # TTS + voice recognition
 ┣ 📂 research/
 ┃ ┗ 📄 user_research_summary.md
 ┣ 📄 README.md
 ┗ 📄 requirements.txt
```

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install opencv-python pyttsx3 SpeechRecognition numpy
```

### Run
```bash
git clone https://github.com/Ozse97/ai-navigation-device.git
cd ai-navigation-device
python software/main.py
```

---

## 👥 Team — JAMBO

| Name | Student ID | Role |
|---|---|---|
| **Ro'zimurodov Ozodbek** | U2410209 | AI/Software Lead, Hardware Integration |
| Ryazanov Bogdan | U2410214 | Hardware Design (Fusion 360) |
| Sagatov Abdfayyoz | U2410215 | User Research |
| Sarsenov Jandaulet | U2410218 | Ideation & Prototyping |
| Rustamov Muhammadamin | U2410210 | Presentation & Documentation |

---

## 📊 Results

- ✅ **Top grade** awarded by course instructor
- ✅ **6 real users** interviewed and incorporated into design
- ✅ **10m obstacle detection range** achieved
- ✅ Fully functional prototype demonstrated

---

## 📄 Presentation

[View Full Canva Presentation](https://www.canva.com/design/DAGmgoRM7cE/eb0-v_aGojJFRVCt-7tJeg/edit)

---

## 📬 Contact

**Ozodbek Ruzimurodov**  
📧 ruzimurodovozodbek5@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/ozodbek-ruzimurodov-931733359/)  
💻 [GitHub](https://github.com/Ozse97)

---

*Built with purpose — for real people, with real needs.*