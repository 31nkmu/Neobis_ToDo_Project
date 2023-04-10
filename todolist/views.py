from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from todolist.models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, 'todolist/index.html', {'todos': todos, 'title': 'Главная страница'})


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    todo = Todo(title=title)
    todo.save()
    return redirect('index')


def update(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.is_completed = not todo.is_completed
    todo.save(update_fields=('is_completed',))
    return redirect('index')


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('index')
