from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from .models import Task


class SignUpForm(UserCreationForm):
    # Email field for the sign-up form
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
            )
        )
    
    # First name field for the sign-up form
    first_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
            )
        )
    
    # Last name field for the sign-up form
    last_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
            )
        )

    class Meta:
        # Meta class to define model and fields
        model = User
        fields = (
            "username", 
            "first_name", 
            "last_name", 
            "email", 
            "password1", 
            "password2",
            )

    def __init__(self, *args: Any, **kwargs):
        # Initialize form and set custom attributes
        super(SignUpForm, self).__init__(*args, **kwargs)

        # Customize username field
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields["username"].help_text = (
            '<span class="form-text text-muted"><small>'
            "Required. 100 characters or fewer digits and @/./+/-/_ only."
            "<small></span>"
        )

        # Customize password1 field
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields["password1"].help_text = (
            '<ul class="form-text text-muted small">'
            "<li>Your password can\'t be too similar to your other personal "
            "information.</li>" 
            "<li>Your password must contain at least 8 characters</li> "
            "<li>Your password can\'t be a commonly used password.</li> "
            "<li>Your password can\'t be entirely numeric.</li> </ul>'"
        )

        # Customize password2 field
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = (
            "Confirm Password"
            )
        self.fields["password2"].label = ""
        self.fields["password2"].help_text = (
            '<span class="form-text text-muted"><small>'
            "Enter the same password as before, for verification."
            "<small></span>"
        )


class TaskForm(forms.ModelForm):
    # Task name field
    name = forms.CharField(
        required=True,
        max_length=50, 
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "", "class":"form-control"}
            ), 
            label="Task Name"
            )
    
    # Task description field
    description = forms.CharField(
        required=True, 
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "", "class":"form-control"}
            ), 
            label="Description")
    
    # Task due date field
    due_date = forms.DateField(
        required=True, 
        widget=forms.widgets.DateInput(
            attrs={
                "placeholder": "", 
                "class":"form-control", 
                "type": "date",
                }
            ), 
            label="Due Date"
            )
    
    def clean_due_date(self):
        # Retrieve the due date from the cleaned form data
        due_date = self.cleaned_data.get("due_date")

        # Check if a due date was provided and if it's in the past
        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError("Due date cannot be in the past.")
        
        # Return the cleaned due date if it's valid
        return due_date
    
    # Task assigned to field
    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        required=True, 
        widget=forms.widgets.Select(
            attrs={"placeholder": "", "class":"form-control"}
            ), 
            label="Assigned To"
            )

    class Meta:
        # Meta class to define model and exclude fields
        model = Task
        exclude = ("user",)