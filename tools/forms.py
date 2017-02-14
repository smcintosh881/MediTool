from django import forms
from tools.models import Tool


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        name = forms.CharField()
        description = forms.__FILL_ME_IN__()
        isAvailable = forms.__FILL_ME_IN__()
        fields = ['name', '__FILL_ME_IN__', '__FILL_ME_IN__']
