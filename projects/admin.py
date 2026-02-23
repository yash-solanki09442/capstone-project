from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "owner", "created_at")
    search_fields = ("title", "slug", "owner__username")
    list_filter = ("created_at",)
    list_select_related = ("owner",)
