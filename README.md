# OpenCV Eye Tracking 👁️

Track and detect eye movements in real-time using **Python** and **OpenCV**.

---

## 📌 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Tips](#tips)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 About

This project uses OpenCV’s **Haar Cascade** classifier to detect eyes and **Hough Circle Transform** to locate pupils.  
It can determine the **direction of gaze** (left/right) in real-time from your webcam feed.

---

## ✨ Features

- Real-time eye detection
- Pupil localization using **HoughCircles**
- Simple gaze direction estimation (left/right)
- Lightweight and easy to run with Python
- Fully open-source

---

## ⚙️ Requirements

- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/) (`cv2`)
- [NumPy](https://numpy.org/)
- `haarcascade_eye.xml` (included in the repo)

---

## 📦 Installation

```bash
git clone https://github.com/Kmmd2003/opencv-eye-tracking.git
cd opencv-eye-tracking
pip install opencv-python numpy
