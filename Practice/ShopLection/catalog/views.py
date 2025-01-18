from django.shortcuts import render, redirect
from catalog.models import Category, Product
from catalog.forms import ContactForm, FeedbackForm
from django.http import HttpResponse



# Create your views here.
# Пример данных (товары с категориями)
products = [
    {'id': 1, 'name': 'Смартфон Samsung Galaxy', 'category': 'телефоны', 'price': 15000},
    {'id': 2, 'name': 'Планшет Apple iPad', 'category': 'планшеты', 'price': 45000},
    {'id': 3, 'name': 'Наушники Sony WH-1000XM4', 'category': 'аксессуары', 'price': 25000},
    {'id': 4, 'name': 'Ноутбук Dell XPS 13', 'category': 'ноутбуки', 'price': 95000},
    {'id': 5, 'name': 'Смарт-часы Xiaomi Mi Band', 'category': 'аксессуары', 'price': 3000},
]

def home(request):
    # Получаем все категории
    categories = Category.objects.all()
    return render(request, 'catalog/home.html',
                  {'categories': categories,
                   })

def product_list(request):
    products = Product.objects.all()  # Получаем все товары из базы данных
    return render(request, 'catalog/product_list.html', {'products': products})

def phones_list(request):
    # Фильтрация товаров по категории "Телефоны"
    products = Product.objects.filter(category__name="Телефоны")
    return render(request,
        'catalog/phones_list.html',
        {'products': products})

def add_product(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        # Добавляем новый товар в список
        products.append({
            'id': len(products) + 1,
            'name': name,
            'category': category,
            'price': int(price),
        })
        # Перенаправляем на список товаров
        return redirect('product_list') # Имя маршрута списка товаров
    # Если GET-запрос, отображаем форму
    return render(request, 'catalog/add_product.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Если форма валидна, обрабатываем данные
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Здесь можно отправить сообщение по email или сохранить в базу данных
            return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    else:
        # GET-запрос, создаём пустую форму
        form = ContactForm()
    return render(request, 'catalog/contact.html', {'form': form})

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Обработка данных
            print(form.cleaned_data)
            return render(request, 'catalog/feedback_success.html')
    else:
        form = FeedbackForm()
    return render(request, 'catalog/feedback_form.html', {'form': form})

def products_by_category(request, category_name):
    # Фильтруем товары по названию категории
    products = Product.objects.filter(category__name=category_name)
    return render(request, 'catalog/products_by_category.html',
                  {'category_name': category_name,'products': products})

def discounted_products(request):
    # Фильтруем товары по цене
    products = Product.objects.filter(price__lt=100000) #price__lt=100000 — фильтрует товары, у которых цена меньше 100 000
    return render(request, 'catalog/discounted_products.html', {'products': products})
