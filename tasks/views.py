from django.shortcuts import render, get_object_or_404
from .models import Task
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormUserNeededMixin, UserOwnerMixin

# Create your views here.

# def task_list_view(request):
#     qs = Task.objects.all()
#     context = {
#         'object_list': qs,
#     }
#     return render(request, 'tasks/task_list.html', context)

class TaskListView(LoginRequiredMixin, ListView):
    model = Task

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        return Task.objects.filter(user=user)



# def task_detail_view(request, pk):
#     obj = get_object_or_404(Task, pk=pk)
#     context = {
#         'object': obj,
#     }
#     return render(request, 'tasks/task_detail.html', context)


class TaskDetailView(UserOwnerMixin, DetailView):
    queryset = Task.objects.all()


# def task_create_view(request):
#     form = TaskForm()
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save()
#             return HttpResponseRedirect(task.get_absolute_url())
#     return render(request, 'tasks/task_form.html', {'form': form})


class TaskCreateView(FormUserNeededMixin, CreateView):
    model = Task
    fields = ['text']

    def get_context_data(self, *args, **kwargs):
        context = super(TaskCreateView, self).get_context_data(*args, **kwargs)
        context['created'] = True
        return context


# def task_update_view(request, pk):
#     obj = get_object_or_404(Task, pk=pk)
#     form = TaskForm(instance=obj)
#     if request.method == 'POST':
#         form = TaskForm(request.POST, instance=obj)
#         if form.is_valid():
#             task = form.save()
#             return HttpResponseRedirect(task.get_absolute_url())
#     return render(request, 'tasks/task_form.html', {'form': form})


class TaskUpdateView(UserOwnerMixin, UpdateView):
    model = Task
    fields = ['text']


# def task_detail_view(request, pk):
#     obj = get_object_or_404(Task, pk=pk)
#     if request.method == 'POST':
#         obj.delete()
#     return render(request, 'tasks/task_confirm_delete', {})

class TaskDeleteView(UserOwnerMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:list')
