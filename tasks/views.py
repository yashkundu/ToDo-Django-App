from django.shortcuts import render, get_object_or_404
from .models import Task
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect
from .forms import TaskForm

# Create your views here.


class TaskListView(ListView):
    queryset = Task.objects.all()


class TaskDetailView(DetailView):
    queryset = Task.objects.all()


class TaskCreateView(CreateView):
    model = Task
    fields = ['text']


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['text']


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:list')
