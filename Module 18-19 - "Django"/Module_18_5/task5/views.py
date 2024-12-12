from django.shortcuts import render
from task5.forms import UserRegister
from django.http import HttpResponse


# Create your views here.
def sign_up_by_django(request):
    users = ['Mik', 'Anna', 'John']
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age <= 17:
                info['error'] = 'Вы должны быть старше 18'
            else:
                return HttpResponse("Форма успешно отправлена.")
    else:
        form=UserRegister()
    return render(request, "fifth_task/registration_page.html", context=info)

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
    return render(request, "fifth_task/registration_page.html")












    # if password == repeat_paswortd:
    #     done
    #     else
    #         "пароли не совпадают"
    # if age > 18:
    #         "вам меньше 18 лет, в доступе к сайту отказано"
#
