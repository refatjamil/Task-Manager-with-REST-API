from django import forms
from .models import Task, Task_Img

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control Roboto', 'placeholder': 'Task Title'}),
            }  
        labels = {
        'title': 'Add Task',

    }

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'd_time']
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control Roboto', 'placeholder': 'Title'}),
        'description': forms.Textarea(attrs={'class': 'custom-class', 'placeholder': 'Description'}),
        'priority': forms.Select(attrs={'class': 'custom-class'}),
        # 'mark': forms.CheckboxInput(attrs={'class': 'custom-class'}),
        'd_time': forms.DateTimeInput(attrs={'class': 'custom-class', 'placeholder': '%Y-%m-%d %H:%M:%S'}),

    }
        labels = {
            'title': 'Task Title',
            'd_time': 'Due Time',
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Task_Img
        fields = ['img']        