# Flask Authentication Project

## Overview
This project is a minimal web application built with **Flask** to demonstrate the basics of user authentication.  
It is designed as an educational example for developers who are starting with Flask and want to learn how sessions, password hashing and database integration work together. 

The application provides a simple login system, a protected dashboard page for authenticated users and a logout function.  
It uses **SQLite** as a lightweight database and **bcrypt** for password hashing to ensure that credentials are stored securely.

## Features
- Login and logout functionality
- Default admin account created on first run
- Secure password storage using bcrypt hashing
- Session-based authentication to protect routes
- Lightweight SQLite database, no external setup required
- Clean, minimal structure suitable for learning and extension

## Installation
To run the project locally, follow these steps:

```bash
#Clone the repository
git clone https://github.com/nikita-lee-222/flask-auth-window
cd flask-auth-window

#Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    #On WinOS: venv\Scripts\activate

#Install dependencies. Just use prepared file or do it by yourself.
pip install -r requirements.txt
```
## Usage
Start the Flask application with:

```bash
python app.py
```

The server will start on http://127.0.0.1:5000. When the app is run for the first time, it creates a default admin user in the database:

```bash
#For security, change the default password before using.
username: admin
password: admin
```

## What can it be used for?
This repository can serve as:
- A starting point for learning Flask and authentication basics
- A boilerplate for small projects that require simple login functionality
- A demonstration of using SQLite and bcrypt with Python

This project was developed with guidance and reference materials from online resources and tools.
