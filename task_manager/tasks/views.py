from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

class Task(View):
    def get(self, request):
        return render(request, 'tasks/tasks.html')
