from django.urls import path

from todolist import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>/', views.update, name='update'),
    path('add/', views.add, name='add'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
