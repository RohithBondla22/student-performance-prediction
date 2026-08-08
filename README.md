# Student Performance Prediction

A beginner-friendly Cloud-Based Machine Learning application that predicts a student's final exam score based on academic information.

## 🌐 Live Demo

**Deployed Application:**
https://student-performance-prediction-5yts.onrender.com/

## 📌 Project Objective

The objective of this project is to build and deploy a Machine Learning model that predicts student performance using academic information such as study hours, attendance, previous exam scores, and completed assignments.

The trained model is integrated with a Flask web application and deployed to the cloud so that users can access the prediction system through a public URL.

## ✨ Features

* Student final score prediction
* Machine Learning model
* Flask REST API
* Web-based user interface
* Input validation
* Performance classification
* Responsive interface
* Cloud deployment
* Publicly accessible application

## 📊 Input Features

The model uses the following information:

| Feature               | Description                     |
| --------------------- | ------------------------------- |
| Study Hours           | Number of hours studied per day |
| Attendance            | Student attendance percentage   |
| Previous Score        | Previous examination score      |
| Assignments Completed | Number of completed assignments |

## 🤖 Machine Learning

**Algorithm:** Linear Regression

The model is trained using student academic data and predicts the student's expected final score.

The prediction result is also classified into performance categories:

* **Excellent** — 85 or above
* **Good** — 70–84
* **Average** — 50–69
* **Needs Improvement** — below 50

## 🏗️ System Architecture

```text
Student
   │
   ▼
Web Interface
   │
   ▼
Flask Application
   │
   ▼
REST Prediction API
   │
   ▼
Machine Learning Model
   │
   ▼
Predicted Final Score
   │
   ▼
Performance Category
```

## 🛠️ Technologies Used

### Programming

* Python

### Machine Learning

* Pandas
* NumPy
* Scikit-learn
* Joblib

### Backend

* Flask
* Gunicorn

### Frontend

* HTML
* CSS
* JavaScript

### Development

* Visual Studio Code
* Git
* GitHub

### Cloud

* Render

## 📁 Project Structure

```text
CloudMLProject/
│
├── data/
│   └── students.csv
│
├── model/
│   └── student_model.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/RohithBondla22/student-performance-prediction.git
```

Move into the project directory:

```bash
cd student-performance-prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Run Locally

Start the Flask application:

```bash
python app.py
```

Open the application:

```text
http://127.0.0.1:5000
```

## ☁️ Cloud Deployment

The application has been deployed using Render.

### Production server

Gunicorn is used as the production WSGI server.

### Build command

```text
pip install -r requirements.txt
```

### Start command

```text
gunicorn app:app
```

### Live application

https://student-performance-prediction-5yts.onrender.com/

## 🧪 Testing

The application was tested with:

### Normal input

```text
Study Hours: 6
Attendance: 85
Previous Score: 72
Assignments: 8
```

Result:

```text
Predicted Score: 77.67
Performance: Good
```

### High-performance input

The application was tested with higher academic values to verify the performance classification.

### Invalid input

The application validates values such as attendance and study hours.

For example:

```text
Attendance: 150
```

produces an appropriate validation error because attendance must be between 0 and 100.

## 📸 Screenshots

Screenshots demonstrating the application, prediction results, project structure, Flask server, and cloud deployment are included as part of the project submission materials.

## 🎯 Project Outcome

The project successfully demonstrates how a Machine Learning model can be integrated into a Flask web application and deployed to the cloud.

The final application is accessible through a public URL and can be used to make student performance predictions.

## 🔮 Future Improvements

Possible future improvements include:

* Adding a larger real-world dataset
* Comparing multiple Machine Learning algorithms
* Adding user authentication
* Storing prediction history
* Adding graphical performance analysis
* Adding a database
* Improving model accuracy
* Adding automated model monitoring

## 👨‍💻 Author

**Rohith Bondla**

GitHub:
https://github.com/RohithBondla22

## 📄 License

This project was created for educational and internship purposes.
