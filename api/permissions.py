from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    - Any authenticated user can READ (safe methods).
    - Only the owner can WRITE.

    Supports objects that:
    - have `owner`, OR
    - are related to a Project via `project.owner` (e.g., Task), OR
    - are related via `task.project.owner` (e.g., Comment)
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # Project has `owner`
        if hasattr(obj, "owner"):
            return obj.owner == request.user

        # Task likely has `project.owner`
        if hasattr(obj, "project") and hasattr(obj.project, "owner"):
            return obj.project.owner == request.user

        # Comment likely has `task.project.owner`
        if (
            hasattr(obj, "task")
            and hasattr(obj.task, "project")
            and hasattr(obj.task.project, "owner")
        ):
            return obj.task.project.owner == request.user

        return False
