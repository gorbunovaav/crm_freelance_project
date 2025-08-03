from django.db import models
from django.conf import settings
from client.models import Client
from client.models import Team
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ("planned", "Planned"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
            ("on_hold", "On Hold"),
            ("cancelled", "Cancelled"),
        ],
        default="planned"
    )
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    project = models.ForeignKey(Project, related_name = 'comments', on_delete=models.CASCADE)
    content = models.TextField(blank = True, null = True)
    created_by = models.ForeignKey(User, related_name='project_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.created_by.username
    

class ProjectFile(models.Model):
    project = models.ForeignKey(Project, related_name = 'files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='projectfiles')
    created_by = models.ForeignKey(User, related_name='project_files', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.created_by.username