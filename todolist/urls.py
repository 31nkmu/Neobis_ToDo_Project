from django.urls import path

from todolist import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='home'),
    path('update/<int:pk>/', views.update, name='update'),
    path('add/', views.CreateTodo.as_view(), name='add'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update_todo/<int:pk>/', views.UpdateTodo.as_view(), name='update_todo')
]
