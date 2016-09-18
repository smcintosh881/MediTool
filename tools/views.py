from tools.models import Tool
from django.shortcuts import render


def index(request):
    tools = Tool.objects.all()
    return render(request, 'tools/index.html', {'tools': tools})
