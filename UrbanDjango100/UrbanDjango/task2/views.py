from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
'''def render_class(request):
    return render(request, 'class_template.html')'''


def render_func(request):
    return render(request, 'second_task/func_template.html')


class RenderClass(TemplateView):
    template_name = 'second_task/class_template.html'
