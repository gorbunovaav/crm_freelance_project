from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from team.models import Team

class Lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    
    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    
    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'
    
    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (WON, 'Won'),
        (LOST, 'Lost'),
    )
    
    name = models.CharField(max_length = 255)
    team = models.ForeignKey(Team, related_name = 'leads', on_delete=models.CASCADE)
    email = models.EmailField()
    description = models.TextField(blank = True, null = True)
    phone =  models.CharField(max_length=12)
    status = models.CharField(max_length = 10, choices=CHOICES_STATUS, default=NEW)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length = 10, choices=CHOICES_PRIORITY, default=MEDIUM)
    converted_to_client = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('name', )
        
    def __str__(self):
        return self.name
    