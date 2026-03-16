from django.contrib import admin
from .models import Task, Category, Status, ListObject


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    search_fields = ("name", "owner")
    list_filter = ("created_at", "owner")


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    search_fields = ("name",)
    list_filter = ("category",)


@admin.register(ListObject)
class ListObjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "category", "status", "rating", "favorite")
    search_fields = ("name",)
    list_filter = ("category", "status", "favorite")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "deadline", "is_completed")
    search_fields = ("title",)
    list_filter = ("is_completed",)
