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
    