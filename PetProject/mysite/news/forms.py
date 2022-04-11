from django import forms
from .models import Comment


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    email = forms.EmailField(label='Введите email адрес', widget=forms.EmailInput(attrs={'class': 'form-control'}))


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name', 'text',
        ]
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}), 'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})}

