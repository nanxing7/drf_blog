from django.shortcuts import render
from django.views.generic import ListView

from .models import ExampleModel


# Create your views here.

# def index(request):
#     e_list = ExampleModel.objects.all()
#     return render(request, template_name='index.html', context={'e_list': e_list})

class ArticleView(ListView):
    model = ExampleModel
    template_name = 'index.html'
    context_object_name = 'e_list'
