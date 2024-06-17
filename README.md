Sticky Notes Application.

The Sticky Notes Application is a Django-based web app that allows users to create, update, and delete tasks.
Users can manage their tasks by setting due dates, assigning tasks to specific users, and tracking task progress.
This project demonstrates key aspects of web development including user authentication, CRUD operations, and dynamic form handling.
Learning these skills is essential for any developer looking to build robust web applications.

* Installation:
To run this project locally, follow these steps:
1. Clone the repository:
git clone https://github.com/VictoriaRau/My_Notes.git

2. Navigate to the project directory:
cd your-repository

3. Create a virtual environment:
python3 -m venv venv

4. Activate the virtual environment:
   
* On Windows:
venv\Scripts\activate

* On macOS and Linux:
source venv/bin/activate

5. Install the required packages:
pip install -r requirements.txt

6. Apply the migrations:
python manage.py migrate

7. Create a superuser to access the admin panel:
python manage.py createsuperuser

8. Run the development server:
python manage.py runserver


* Usage:

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
