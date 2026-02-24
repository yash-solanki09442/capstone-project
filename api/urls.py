from django.urls import include, path

from . import views

urlpatterns = [
    # Test health check
    path("health/", views.health, name="health"),
    # App urls
    path("", include("projects.urls")),
    path("", include("tasks.urls")),
    path("", include("comments.urls")),
]
