import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

from users.forms import RegisterForm, LoginForm
import logging
from django.core.cache import cache
from django.shortcuts import render

from django.db.models import Q
from products.models import Hotels, Product

logger = logging.getLogger(__name__)


def users(request):
    if request.GET.get("param"):
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Profiles view")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:

        form = RegisterForm()


    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")




def hotels(request):
    title = request.GET.get("title")
    purchases__count = request.GET.get("purchases__count")

    result = cache.get(f"products-view-{title}-{purchases__count}-{request.user.id}")
    if result is not None:
        return result

    hotels = Hotels.objects.all()

    if title is not None:
        hotels = hotels.filter(title__icontains=title)

    if purchases__count is not None:
        hotels = hotels.filter(purchases__count=purchases__count)

    response = render(request, "index.html", {"products": hotels})
    cache.set(f"products-view-{title}-{purchases__count}", response, 60 * 60)
    return response


def hotels(request):
    search = request.GET.get("search")

    hotels = Hotels.objects.all()

    if search is not None:
        hotels = hotels.filter(Q(title__icontains=search) | Q(description__icontains=search))

    response = render(request, "index.html", {"products": hotels})
    return response




def onehotel(request, hotel_id):
    title = request.GET.get("title")
    purchases__count = request.GET.get("purchases__count")

    result = cache.get(f"products-view-{title}-{purchases__count}-{request.user.id}")
    if result is not None:
        return result

    onehotel = Product.objects.filter(id=hotel_id)

    if title is not None:
        onehotel = Product.filter(title__icontains=title)

    if purchases__count is not None:
        onehotel = Product.filter(purchases__count=purchases__count)

    response = render(request, "index.html", {"products": onehotel})
    cache.set(f"products-view-{title}-{purchases__count}", response, 60 * 60)
    return response

def onehotel(request, hotel_id):
    search = request.GET.get("search")

    onehotel = Product.objects.filter(id=hotel_id)

    if search is not None:
        onehotel = onehotel.filter(Q(title__icontains=search) | Q(description__icontains=search) | Q(price__icontains=search))



    response = render(request, "index.html", {"products": onehotel})
   
    return response