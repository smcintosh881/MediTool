from django import forms
from tools.models import Tool


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        name = forms.CharField()
        description = forms.CharField()
        isAvailable = forms.BooleanField()
        fields = ['name', 'description', 'isAvailable']
