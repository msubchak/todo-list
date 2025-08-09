from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Tag, Task


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todo_list/tag_form.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    template_name = "todo_list/tag_delete.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.all().order_by("is_complete", "-datetime")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:task-list")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "todo_list/task_delete.html"
    success_url = reverse_lazy("todo_list:task-list")


def task_status(request: HttpRequest, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_complete = not task.is_complete
    task.save()
    return redirect("todo_list:task-list")
