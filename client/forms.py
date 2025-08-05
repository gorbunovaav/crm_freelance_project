from django import forms 

from .models import Client, Comment, ClientFile

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ("name", "email", "phone", "description")
        labels = {
            'name': 'Имя',
            'email': 'Электронная почта',
            'phone': 'Телефон',
            'description': 'Описание',
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
        model = ClientFile
        fields = ("file",)