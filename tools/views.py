from tools.models import Tool
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, __FILL_ME_IN__
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
    template_name = 'tools/tool_form.html'

    form_class = ToolForm

class EditTool(__FILL_ME_IN__):
    
    model = Tool
    template_name = 'tools/__FILL_ME_IN__.html'

    form_class = __FILL_ME_IN__
