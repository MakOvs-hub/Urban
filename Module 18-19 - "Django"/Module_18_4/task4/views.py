from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request, "fourth_task/main.html")

def buy(request):
    first  = "Atomic Heart"
    second = "Cyberpunk 2077"
    third = "Heart og Iron IV"
    context = {
        'first': 'Atomic Heart',
        'second': "Cyberpunk 2077",
        'third' : "Heart og Iron IV",
    }
    return render(request, "fourth_task/shop.html", context)

def sold(request):
    return render(request, "fourth_task/gift.html")

def menu(request):
    return render(request, "fourth_task/menu.html")