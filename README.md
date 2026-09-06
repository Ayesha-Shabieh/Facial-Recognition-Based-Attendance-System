# Facial Recognition Based Attendance System

A comprehensive, modular desktop application built in Python that automates attendance tracking using computer vision. The system provides an interactive graphical interface to manage student enrollments, train biometric face models using the **LBPH** algorithm, and record real-time attendance logs directly into a **MySQL** database.

## Co-Authors (50/50 Credit)
This project was co-developed equally from scratch by:
* **Ayesha Ahmad** - (https://Github.com/Ayesha-is-coding)
* **Shabieh Batool** - (https://Github.com/Shabiehbtl)

## Key Modules
The project is built with a modular architecture broken down into the following files:
* `project.py` — The primary entry point that launches the main Tkinter dashboard.
* `b1_student.py` — Management panel to add, update, and remove student enrollment records.
* `b2_traindata.py` — Scripts to train the classifier using extracted facial landmarks.
* `b3_face_detection.py` — The core engine executing real-time webcam streaming and LBPH facial verification.
* `b5_attendance.py` — Interface to view, fetch, and clear local attendance logs.
* `b6_developer.py` & `b7_help.py` — Support panels containing developer details and troubleshooting steps.

## Tech Stack
* **GUI Frontend:** Python Tkinter
* **Computer Vision Processing:** OpenCV (`opencv-python` with `cv2.face.LBPHFaceRecognizer`)
* **Database Backend:** MySQL
* **Image Utilities:** Pillow (PIL), NumPy

## Prerequisites & Local Setup

### 1. Database Configuration
Because this system relies on a central database, you must configure a local MySQL instance before running the app:
1. Open your MySQL Workbench or command line tool.
2. Ensure you have a database schema ready. *(Update the database name, host, user, and password credentials within the python script files if they differ from your defaults).*
3. Create your target tables for `student` records and `attendance` logging.

### 2. Dependency Installation
Since you are setting up a fresh environment, open your terminal/command prompt and install the required modules:
```bash
pip install opencv-python opencv-contrib-python pillow numpy mysql-connector-python
```
*(Note: `opencv-contrib-python` is explicitly required to access the built-in LBPH face recognition modules).*

### 3. Running the Application
Always launch the project by executing the primary script:
```bash
python project.py
```

## Application Workflow
1. **Student Registration (`b1_student.py`):** Input details to save metadata to MySQL and trigger the webcam to capture sample face images.
2. **Model Training (`b2_traindata.py`):** Train the LBPH classifier on your image dataset to recognize the registered patterns.
3. **Attendance Logging (`b3_face_detection.py`):** Activate live video recognition. Recognized faces immediately trigger a secure write action to mark attendance logs in the database.
