# Sticky Notes Application

The Sticky Notes Application is a Django-based web app that allows users to create, update, and delete tasks. Users can manage their tasks by setting due dates, assigning tasks to specific users, and tracking task progress. This project demonstrates key aspects of web development including user authentication, CRUD operations, and dynamic form handling. Learning these skills is essential for any developer looking to build robust web applications.

## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Credits](#credits)

## Description
The Sticky Notes Application is designed to help users manage their tasks efficiently. Users can:
- Create new tasks with specific details like name, description, due date, and assigned user.
- Update existing tasks to reflect any changes.
- Delete tasks that are no longer needed.
- View all tasks in a list format, displaying their details and status.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/VictoriaRau/My_Notes.git

2. **Navigate to the project directory:**
   ```bash
   cd your-repository

3. **Create a virtual environment:**
   ```bash
   python3 -m venv venv

4. **Activate the virtual environment:**
   
* On Windows:
   ```bash
   venv\Scripts\activate

* On macOS and Linux:
  ```bash
   source venv/bin/activate

5. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

6. **Apply the migrations:**
   ```bash
   python manage.py migrate

7. **Create a superuser to access the admin panel:**
   ```bash
   python manage.py createsuperuser

8. **Run the development server:**
   ```bash
   python manage.py runserver

## Usage:

1. Login/Register:
Access the app through your browser at http://127.0.0.1:8000/. Register a new user or log in with your credentials.

2. Creating a Task:
Navigate to the "Create Task" page and fill in the details of your task, including the name, description, due date, and assigned user.

3. Updating a Task:
From the task list, click on a task to edit its details.


4. Deleting a Task:
Click the delete button next to a task in the list to remove it.


5. Viewing Tasks:
View all your tasks on the homepage, where they are listed with their details and status.


## Credits:
Developed by Victoria Rau. 
Special thanks to the Django documentation and the open-source community for their invaluable resources and support.


