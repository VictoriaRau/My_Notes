from django.urls import path
from . import views

# URL patterns for the app
urlpatterns = [
    # Home page, handles login
    path("", views.home, name = "home"),
    # Logout user
    path("logout/", views.logout_user, name = "logout"),
    # Register new user
    path("register/", views.register_user, name = "register"),
    # View a specific task
    path("task/<int:pk>", views.task_record, name = "task"),
    # Delete a task
    path("delete_task/<int:pk>", views.delete_task, name = "delete_task"),
    # Add a new task
    path("add_task/", views.add_task, name = "add_task"),
    # Update a task
    path("update_task/<int:pk>", views.update_task, name = "update_task"),

]