# 📝 Complete Todo App

A simple and beginner-friendly Todo application built with **Python Flask** and **HTML**. This project allows users to create, view, update, and delete tasks while learning the fundamentals of backend development with Flask.

## 🚀 Features

* ✅ Add new tasks
* 📋 View all tasks
* ✏️ Update existing tasks
* ❌ Delete tasks
* 💾 Store data locally
* 🌐 Simple HTML frontend
* 🐍 Flask backend

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Data Storage:** JSON file / In-memory data
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
complete-todo/
│
├── app.py
├── db.json
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── README.md
└── venv/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/complete-todo.git
cd complete-todo
```

### Create virtual environment

```bash
python3 -m venv venv
```

### Activate virtual environment

#### Mac/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install flask
pip install gunicorn
```

---

## ▶️ Run the application

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:5000/
```

---

## 📌 API Endpoints

| Method | Endpoint          | Description   |
| ------ | ----------------- | ------------- |
| GET    | /                 | Home Route    |
| GET    | /todos            | Get All Tasks |
| POST   | /todo/create      | Create Task   |
| PUT    | /todo/update/<id> | Update Task   |
| DELETE | /todo/delete/<id> | Delete Task   |

---

## 📚 What I Learned

* Flask routing
* HTTP methods (GET, POST, PUT, DELETE)
* Handling JSON data
* CRUD operations
* Building APIs with Flask
* Integrating HTML with Flask
* Using Git and GitHub for version control

---

## Future Improvements

* Add SQLite database
* User authentication
* Search tasks
* Task categories
* Due dates and reminders
* Responsive UI with Bootstrap

---

## Author

**Kirti Shinde**

Frontend Developer | Learning Python & Flask 🚀
