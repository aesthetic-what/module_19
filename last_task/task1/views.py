from django.shortcuts import render
from django.core.paginator import Paginator
from task1.forms import UserRegister
from .models import Buyer, Game, News

# Create your views here.
def menu(request):
    return render(request, 'task1/menu.html')

def main(request):
    return render(request, 'task1/main.html')

def shop(request):
    # titles = Game.title
    # descriptions = Game.description
    # costs = Game.cost
    
    Games = Game.objects.all()
    
    # context = {
    #     'titles': titles,
    #     'descriptions': descriptions,
    #     'costs': costs
    #     }
    context = {
        'games': Games
    }
    
    return render(request, 'task1/shop.html', context)

def cart(request):
    cont = 'Продолжить покупки'
    done = 'Оформить заказ'
    context = {
        'cont': cont,
        'done': done,

    }
    
    return render(request, 'task1/cart.html', context)

users = Buyer.objects.all()

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return render(request,
                              'task1/registration_page_by_django.html',
                              {'form': form, 'info': f"Приветствуем, {username}!"})
    else:
        form = UserRegister()
    return render(request,
                  'task1/registration_page_by_django.html',
                  {'form': form, 'info': info.get('error')})

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return render(request,
                          'task1/registration_page.html',
                          {'info': f"Приветствуем, {username}!"})
    return render(request,
                  'task1/registration_page.html',
                  {'info': info.get('error')})
    
def news(request):
    news = News.objects.all()
    
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'task1/news.html', {'page_obj': page_obj})
    