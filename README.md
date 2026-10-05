# SmartScan – OCR-Based Task and Reminder Assistant

##  Project Description

SmartScan is an OCR-based task and reminder application developed using Python and Streamlit.

The application allows users to upload an image containing text. OCR is used to extract the text from the image. The extracted text can be used as a task, along with a date and reminder time.

The tasks are stored in a SQLite database and users can manage their tasks easily.

---
## Live Demo
https://smartscanocr-based-personal-task-and-remainder-assistant-6of6s.streamlit.app/

##  Objectives

* Extract text from images using OCR.
* Convert extracted text into a task.
* Add a date and reminder time.
* Store tasks in a database.
* View all saved tasks.
* Mark tasks as completed.
* Delete tasks when they are no longer needed.

---

##  Technologies Used

* Python
* Streamlit
* EasyOCR
* Pillow
* SQLite
* NumPy

---

##  Project Structure

```text
SmartScan/
│
├── app.py
├── ocr.py
├── database.py
├── reminder.py
├── requirements.txt
└── README.md
```

---

##  Project Workflow

```text
Upload Image
      ↓
     OCR
      ↓
Extract Text
      ↓
   Create Task
      ↓
Select Date and Time
      ↓
 Save Task in Database
      ↓
 View / Complete / Delete Task
```

---

##  Features

### 1. Image Upload

Users can upload images in JPG, JPEG, or PNG format.

### 2. OCR Text Extraction

The application uses OCR to detect and extract text from the uploaded image.

### 3. Task Creation

The extracted text can be used as the task name.

Users can also select:

* Task Date
* Reminder Time

### 4. Task Management

Users can:

* View tasks
* Complete tasks
* Delete tasks

### 5. Database Storage

SQLite database is used to store task information.

---

##  Installation

### Step 1: Clone the Project

```bash
git clone https://github.com/your-username/SmartScan.git
```

### Step 2: Open the Project Folder

```bash
cd SmartScan
```

### Step 3: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### Step 5: Install Required Packages

```powershell
python -m pip install -r requirements.txt
```

---

##  Run the Application

Run the following command:

```powershell
python -m streamlit run app.py
```

The application will open in the browser.

---

##  Example

Suppose the uploaded image contains:

```text
Complete DBMS Assignment
Submit on Monday
```

OCR extracts the text:

```text
Complete DBMS Assignment
Submit on Monday
```

The user can then create a task and select the required date and time.

---

##  Database

The application uses SQLite to store task information.

The database contains:

* Task ID
* Task Name
* Task Date
* Task Time
* Task Status

The database file `tasks.db` is created automatically when the application runs.

---

##  Requirements

The `requirements.txt` file contains the required Python libraries:

```text
streamlit
easyocr
Pillow
torch
torchvision
```

---

##  Deployment

The application can be deployed using Streamlit Community Cloud.

For deployment:

1. Upload the project to GitHub.
2. Open Streamlit Community Cloud.
3. Select the GitHub repository.
4. Select `app.py` as the main file.
5. Deploy the application.

---

##  Future Enhancements

* Automatic reminder notifications.
* Voice-based task creation.
* Support for multiple languages.
* Better OCR accuracy.
* Task priority levels.
* Task categories.
* Email notifications.
* Mobile application support.

##  License

This project is developed for educational purposes.
