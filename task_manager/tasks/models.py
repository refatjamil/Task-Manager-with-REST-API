from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),

       ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now=True)
    d_time = models.DateTimeField(null=True, blank=True)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        null=True,
        blank=True
    )
    mark = models.BooleanField(default=False)


class Task_Img(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="task_img")


