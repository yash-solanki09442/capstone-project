from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    # JWT auth endpoints
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Test health check
    path("health/", views.health, name="health"),
    # App urls
    path("", include("projects.urls")),
    path("", include("tasks.urls")),
    path("", include("comments.urls")),
]
