from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request, "third_task/main.html")

def buy(request):
    return render(request, "third_task/shop.html")

def sold(request):
    return render(request, "third_task/gift.html")