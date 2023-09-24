from django.shortcuts import render, redirect
from django.views import View
from .models import Task, Task_Img
from .forms import TaskForm, TaskUpdateForm, PhotoForm
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse

class TaskListView(View):
    template_name = 'tasks/tasks.html'

    def get(self, request):
        tasks = Task.objects.all().filter(user=request.user)
        form = TaskForm()
        context = {'task_list': tasks, 'form': form}
        return render(request, self.template_name, context)


class TaskDetailsView(View):
    template_name = 'tasks/task_details.html'

    def get(self, request, pk):
        try:
            tasks = Task.objects.get(pk=pk, user=request.user)
            task_img = Task_Img.objects.all().filter(task=pk)
            context = {'task': tasks, 'task_img': task_img}
        except Task.DoesNotExist:
            return redirect('/')
        
        return render(request, self.template_name, context)
 
    
class TaskCreateView(CreateView):
    # specify the model you want to use
    model = Task
    form_class = TaskForm

    success_url ="/"
     
    template_name = 'tasks/tasks.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user to the current logged-in user
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    # specify the model you want to use
    model = Task
    form_class = TaskUpdateForm
    def get_success_url(self):
        # Redirect to the 'more_details' URL with the primary key (ID) of the created object
        return reverse('more_details', args=[self.object.pk])   
      
    template_name = 'tasks/task_update.html'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user to the current logged-in user
        return super().form_valid(form)   

    
class TaskDeleteView(DeleteView):
    # specify the model you want to use
    model = Task

    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url ="/"
     
    template_name = 'tasks/tasks.html'


def add_photo(request, id):
    if request.method == 'POST':

        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            task = Task.objects.get(pk=id)
            img = form.cleaned_data['img']
            img_form = Task_Img(task=task, img=img)
            img_form.save()
            return redirect(f'/more_details/{id}/')  # Redirect to a view that displays the list of photos
    else:
        form = PhotoForm()

    context = {'form': form}
        
    return render(request, 'tasks/add_photo.html', context)

def delete_photo(request,id):
    if request.method == 'POST':
        task_id = Task_Img.objects.get(pk=id).task.id

        pi = Task_Img.objects.get(pk=id)
        pi.delete()
        return redirect(f'/more_details/{task_id}/')

    return render(request, 'tasks/task_details.html') 

def complete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(pk=id)
        if task.mark:
            task.mark = False
            task.save()

            return redirect('/')
        else:
            task.mark = True
            task.save()
            return redirect('/')  
    return render(request, 'tasks/tasks.html')