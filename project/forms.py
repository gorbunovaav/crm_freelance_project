from django import forms 

from .models import Project, ProjectFile

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "description", "budget", "status", 'team', 'start_date', 'end_date')
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'end_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['start_date', 'end_date']:
            self.fields[field].input_formats = ['%Y-%m-%d']


class AddFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ("file",)