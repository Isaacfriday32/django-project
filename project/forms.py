from django import forms
from .models import ProjectFormat


class AddNewProject(forms.ModelForm):

    class Meta:
        model = ProjectFormat
        fields = ["title", "description", "tech_stack","programmer", "image", "project_link"]

    
