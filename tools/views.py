from tools.models import Tool
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from tools.models import Tool
from tools.forms import ToolForm
from django.http import HttpResponseRedirect

def index(request):
    tools = Tool.objects.all()
    return render(request, 'tools/index.html', {'tools': tools})


def detail(request, tool_id):
    tool = get_object_or_404(Tool, pk=tool_id)
    return render(request, 'tools/detail.html', {'tool': tool})


class CreateTool(CreateView):

    model = Tool
    # fields = ['name', 'description', is ]
    template_name = 'tools/tool_form.html'

    form_class = ToolForm

