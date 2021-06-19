from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'title_tag', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Add title...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tag...'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type your story here...'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ('title', 'title_tag', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Add title...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Tag...'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type your story here...'})
        }