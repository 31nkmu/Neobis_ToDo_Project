from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import UpdateView, ListView, CreateView

from todolist.forms import CreateTodoForm
from todolist.models import Todo


class TodoList(ListView):
    model = Todo
    template_name = 'todolist/index.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.all().order_by('id')


class CreateTodo(CreateView):
    form_class = CreateTodoForm
    template_name = 'todolist/index.html'
    success_url = reverse_lazy('home')


class UpdateTodo(UpdateView):
    model = Todo
    template_name = 'todolist/update_todo.html'
    fields = ('title', 'description')
    success_url = reverse_lazy('home')


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.is_completed = not todo.is_completed
    todo.save(update_fields=('is_completed',))
    return redirect('home')


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('home')
