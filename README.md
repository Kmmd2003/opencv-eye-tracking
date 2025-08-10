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

## ▶️ Usage
- Run the main script:
python eye_control.py


## 🛠 How It Works
1.Capture a frame from the webcam

2.Convert the frame to grayscale

3.Apply histogram equalization and blurring for better detection

4.Detect eyes using Haar Cascade

5.Detect pupils using Hough Circle Transform

6.Calculate the pupil position relative to the eye center

7.Determine gaze direction (left/right)


## 💡 Tips
- Good lighting significantly improves detection accuracy

- Adjust HoughCircles parameters for your specific webcam

- For more accurate gaze tracking, consider integrating Dlib facial landmarks or Google MediaPipe

## 🚀 Roadmap

| Feature                      | Description                                          |
| ---------------------------- | ---------------------------------------------------- |
| More accurate gaze detection | Use facial landmarks for better precision            |
| Blink detection              | Detect eye blinks for control/interaction            |
| GUI support                  | Add a user-friendly control panel                    |
| Multi-platform support       | Make it work seamlessly on Linux, Windows, and macOS |

## 🤝 Contributing
Contributions are welcome!
Feel free to open issues or submit pull requests to improve the project.

## 📜 License
This project is licensed under the GPL-3.0 License.
See the LICENSE file for details.
