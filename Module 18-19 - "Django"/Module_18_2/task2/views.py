from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, "Func.html")

class IndexClass(TemplateView):
    template_name = "Class.html"