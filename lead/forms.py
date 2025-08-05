from django import forms 

from .models import Lead, Comment, LeadFile

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ("name", "email", "phone", "description", 'priority', 'status',)
        labels = {
            'name': 'Имя',
            'email': 'Электронная почта',
            'phone': 'Телефон',
            'description': 'Описание',
            'priority': 'Приоритет',
            'status': 'Статус',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control form-control-sm"

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)

class AddFileForm(forms.ModelForm):
    class Meta:
        model = LeadFile
        fields = ("file",)