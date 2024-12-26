from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game, News


def index(request):
    punkt = ['Главная', 'Магазин', 'Корзина']
    data = {'punkt_menu': punkt}
    return render(request, "first_task/index.html", context=data)


def market(request):
    #context_market = {'games': ['Snow spinner', 'Dcs word', 'I76']}
    games = list(Game.objects.all())
    data = {'games':games}
    return render(request, "first_task/market.html", context=data)


def cart(request):
    return render(request, "first_task/cart.html")


# Create your views here.

info = {}


def check_user(users: list, name: str, pas: str, rep_pas: str, age: int) -> bool:
    if (name not in users) and (pas == rep_pas) and int(age) > 18:
        return True


def sign_up_by_html(request):
    global info
    usersname = []
    users = list(Buyer.objects.all())
    for user in users:
        usersname.append(user.name)
    if request.method == 'POST':
        username = request.POST.get('username').capitalize()
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if check_user(usersname, username, password, repeat_password, age):
            return HttpResponse(f'Приветствуем, {username}!')
        if username in usersname:
            info = {'error': 'Пользователь уже существует'}
        if int(age) < 18:
            info = {'error': 'Вы должны быть старше 18'}
        if password != repeat_password:
            info = {'error': 'Пароли не совпадают'}
    return render(request, 'first_task/registration_page.html', context=info)





def sign_up_by_django(request):
    global info
    usersname = []
    users = list(Buyer.objects.all())
    for user in users:
        usersname.append(user.name)

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].capitalize()
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username in usersname:
                info = {'error': 'Пользователь уже существует'}

            if check_user(usersname, username, password, repeat_password, int(age)):
                Buyer.objects.create(name=username, age=int(age), balance=0)
                return HttpResponse(f'Приветствуем, {username}!')

            elif int(age) < 18:
                info = {'error': 'Вы должны быть старше 18'}
            elif password != repeat_password:
                info = {'error': 'Пароли не совпадают'}
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'first_task/registration_page.html', context=info)

def news(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'first_task/news.html',{'page_obj':page_obj})
