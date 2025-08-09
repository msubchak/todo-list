from django.contrib import admin

from todo.models import Task, Tag

admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "datetime",
        "deadline",
        "is_complete",
    )
