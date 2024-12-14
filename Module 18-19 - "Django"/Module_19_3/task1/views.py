from django.shortcuts import render
from task1.forms import UserRegister
from django.http import HttpResponse
from task1.models import *


# Create your views here.
def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            for user in users:
                if username == user.name:
                    info['error'] = 'Пользователь уже существует'
                    return HttpResponse(info['error'])
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse(info['error'])
            elif age <= 17:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse(info['error'])
            else:
                Buyer.objects.create(name =username, balance = 1000, age=age)
                return HttpResponse("Форма успешно отправлена.")
    else:
        form=UserRegister()
    return render(request, "first_task/registration_page.html", context=info)

def sign_up_by_html(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        print(f"Username:{username}")
        print(f"password:{password}")
        print(f"repeat_password:{repeat_password}")
        print(f"age:{age}")

        return HttpResponse("Форма успешно отправлена.")
    return render(request, "first_task/registration_page.html")

def start(request):
    return render(request, "first_task/main.html")

def buy(request):
    games = Game.objects.all()
    info_game = []
    for game in games:
        i = 0
        if i != len(games):
            j = f'{game.title} | {game.description}. Стоимость: {game.cost}'
            info_game.append(j)
            i += 1

    context = {
        'game1': f'{info_game[0]}',
        'game2': f'{info_game[1]}',
        'game3': f'{info_game[2]}',

    }
    return render(request, "first_task/shop.html", context)

def sold(request):
    return render(request, "first_task/gift.html")

def menu(request):
    return render(request, "first_task/menu.html")