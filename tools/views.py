from tools.models import Tool
from django.shortcuts import render, get_object_or_404


def index(request):
    tools = Tool.objects.all()
    return render(request, 'tools/index.html', {'tools': tools})

def detail(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    return render(request, 'tools/detail.html', {'tool': tool})
