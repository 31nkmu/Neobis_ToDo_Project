from django import forms

from todolist.models import Todo


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'deadline')
