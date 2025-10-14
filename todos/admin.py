from django.contrib import admin

# Register your models here.
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "created_at", "updated_at")
    list_filter = ("completed", "created_at", "updated_at")
    search_fields = ("title", "description")
    ordering = ("-created_at",)
