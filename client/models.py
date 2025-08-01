from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from team.models import Team


class Client(models.Model):
    name = models.CharField(max_length = 255)
    team = models.ForeignKey(Team, related_name = 'clients', on_delete=models.CASCADE)
    email = models.EmailField()
    description = models.TextField(blank = True, null = True)
    phone =  models.CharField(max_length=12)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name', )
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    team = models.ForeignKey(Team, related_name = 'client_comments', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name = 'comments', on_delete=models.CASCADE)
    content = models.TextField(blank = True, null = True)
    created_by = models.ForeignKey(User, related_name='client_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.created_by.username

class ClientFile(models.Model):
    team = models.ForeignKey(Team, related_name = 'client_files', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name = 'files', on_delete=models.CASCADE)
    file = models.FileField(upload_to='lclientfiles')
    created_by = models.ForeignKey(User, related_name='client_files', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.created_by.username