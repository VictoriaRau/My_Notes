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

#### 1. Login/Register:
Access the app through your browser at http://127.0.0.1:8000/. Register a new user or log in with your credentials.

<picture>
 <img alt="Login" src="https://github.com/VictoriaRau/My_Notes/blob/main/Login.png">
</picture>

#### 2. Creating a Note:
Navigate to the "Add Note" page and fill in the details of your task, including the name, description, due date, and assigned user.

<picture>
 <img alt="New" src="https://github.com/VictoriaRau/My_Notes/blob/main/New.png">
</picture>

#### 3. Updating a Note:
From the notes list, click on a note to edit its details.

<picture>
 <img alt="Update" src="https://github.com/VictoriaRau/My_Notes/blob/main/Update.png">
</picture>

#### 4. Deleting a Note:
Click the delete button next to a note in the list to remove it.

<picture>
 <img alt="Delete" src="https://github.com/VictoriaRau/My_Notes/blob/main/Delete.png">
</picture>

#### 5. Viewing Notes:
View all your notes on the homepage, where they are listed with their details and status.

<picture>
 <img alt="List" src="https://github.com/VictoriaRau/My_Notes/blob/main/List.png">
</picture>


## Credits:
Developed by Victoria Rau. 
Special thanks to the Django documentation and the open-source community for their invaluable resources and support.


