from django.contrib import admin
from django.urls import path, include

# URL patterns for the project
urlpatterns = [
    # Admin site
    path("admin/", admin.site.urls),
    # Include URLs from the 'my_notes' app
    path("", include("my_notes.urls")),
]
