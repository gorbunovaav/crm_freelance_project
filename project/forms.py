from django import forms 

from .models import Project, Comment, ProjectFile

class AddProjectForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Project
        fields = ("name", "description", "budget", "status", 'team', 'start_date', 'end_date')
        # widgets = {
        #     'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        #     'end_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        # }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in ['start_date', 'end_date']:
    #         self.fields[field].input_formats = ['%Y-%m-%d']

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)

class AddFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ("file",)