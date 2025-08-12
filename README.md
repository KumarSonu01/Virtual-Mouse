# 🖱️ Virtual Mouse using Hand Tracking

A Python-based virtual mouse that uses your webcam to track hand movements and control the cursor in real-time.  
Built with **OpenCV**, **MediaPipe**, and **PyAutoGUI**.

## ✨ Features
- Hand tracking using **MediaPipe**
- Smooth cursor movement
- Click by pinching your thumb and index finger together
- Adjustable pinch sensitivity
- Works on Windows, macOS, and Linux

## 📸 Demo
*(Add a screenshot or GIF here after recording your demo)*

## 🛠️ Requirements
- Python 3.8 – 3.11 (Recommended: Python 3.10.11)
- Webcam
- pip (Python package manager)

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/virtual-mouse.git
cd virtual-mouse
```

2. **Create a virtual environment**
```bash
python -m venv .venv
```
3. **Activate the environment**
   For Windows
```bash
.\.venv\Scripts\activate
```
  For MacOS/Linux
```bash
source .venv/bin/activate
```
4. **Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
▶️ Usage
**Run the script:**
```bash
python virtual_mouse.py
```
**Instructions**
1. Index finger movement → moves the mouse cursor.
2. Thumb + Index pinch → left click.
3. Esc key → exit.

⚠️ Notes
Mediapipe does not currently support Python 3.13, use Python 3.8–3.11.

Ensure good lighting for better tracking.

Close other apps using your webcam before running.

📜 License
This project is licensed under the MIT License.
