# uploadapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Document, CustomUser, IPOChecklist

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['field_name', 'file']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class IPOChecklistForm(forms.ModelForm):
    class Meta:
        model = IPOChecklist
        exclude = ['user', 'uploaded_at']

