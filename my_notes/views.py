from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, TaskForm
from .models import Task


def home(request):
    """Render the home page and handle login."""
    tasks = Task.objects.all()

    # Check if loggin in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate user
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in! ")
            return redirect("home")
        else:
            messages.error(
                request, 
                "There was an error logging in. Please try again."
                )
            return redirect("home")
    else:
        return render(request, "home.html", {"tasks": tasks})


def logout_user(request):
    """Log out the user."""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


def register_user(request):
    """Register a new user."""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and login new user
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(
                request, 
                username = username, 
                password = password
                )
            login(request, user)
            messages.success(
                request, 
                "You Have Successfully Registered. Welcome!"
                )
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form":form})
    return render(request, "register.html", {"form":form})


def task_record(request, pk):
    """View a specific task record."""
    if request.user.is_authenticated:
        # Look Up Records
        task_record = Task.objects.get(id=pk)
        return render(request, "task.html", {"task_record":task_record})
    else: 
        messages.error(request, "You must be logged in to view notes list.")
        return redirect("home")


def delete_task(request, pk):
    """Delete a task."""
    if request.user.is_authenticated:
        delete_it = Task.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Note Deleted Successfully")
        return redirect("home")
    else:
        messages.error(request, "You must be logged in to delete a note.")
        return redirect("home")
    

def add_task(request):
    """Add a new task."""
    if request.user.is_authenticated:
        form = TaskForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            add_task = form.save(commit=False)
            add_task.user = request.user
            add_task.save()
            messages.success(request, "Note Added")
            return redirect("home")
        return render(request, "add_task.html", {"form": form})
    else:
        messages.error(request, "You must be logged in to add a note.")
        return redirect("home")
    

def update_task(request, pk):
    """Update an existing task."""
    if request.user.is_authenticated:
        current_task = Task.objects.get(id=pk)
        form = TaskForm(request.POST or None, instance=current_task)
        if form.is_valid():
            form.save()
            messages.success(request, "Note Has Been Updated!")
            return redirect("home")
        return render(request, "update_task.html", {"form": form})
    else:
        messages.error(request, "You must be logged in to update a note.")
        return redirect("home")