import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from projects.models import Project
from tasks.models import Task

User = get_user_model()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="testuser", email="test@example.com", password="password123"
    )


@pytest.fixture
def project(user):
    return Project.objects.create(title="Test Project", owner=user)


@pytest.fixture
def task(project, user):
    return Task.objects.create(
        title="Test Task", project=project, assignee=user, status="todo"
    )


@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client
