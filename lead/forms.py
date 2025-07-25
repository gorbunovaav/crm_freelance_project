from django import forms 

from .models import Lead

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ("name", "email", "phone", "description", 'priority', 'status')
