import logging

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

from users.forms import RegisterForm, LoginForm, BookingForm, ScoreForm
import logging
from django.core.cache import cache
from django.shortcuts import render

from django.db.models import Q
from products.models import Hotels, Product, ProductImage, Comment
from users.forms import CommentForm

from django.core.mail import send_mail
from django.conf import settings



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

def countries(request):
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

def countries(request):

    search = request.GET.get("search")

    countries = Hotels.objects.all()

    if search is not None:
        countries = countries.filter(Q(title__icontains=search) | Q(description__icontains=search))

    response = render(request, "countries.html", {"countries": countries})
    return response

def oneHotel(request, hotel_id):
    title = request.GET.get("title")
    purchases__count = request.GET.get("purchases__count")

    oneHotel = Product.objects.filter(id=hotel_id)

    if title is not None:
        oneHotel = Product.filter(title__icontains=title)

    if purchases__count is not None:
        oneHotel = Product.filter(purchases__count=purchases__count)

    response = render(request, "oneHotel.html", {"oneHotel": oneHotel})
    return response

def oneHotel(request, hotel_id):
    search = request.GET.get("search")

    oneHotel = Product.objects.get(id=hotel_id)
    images = ProductImage.objects.all()
    comments = oneHotel.comments.all()
    if hotel_id is not None:
        images = images.filter(product_id=hotel_id)

    response = render(
        request, 
        "oneHotel.html", 
        {
            "oneHotel": oneHotel, 
            "images": images, 
            "comments": comments
        }
    )
   
    return response

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request=request,
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            
            send_mail(
                "Подтверждение брони", 
                "Вы успешно забронировали отель!", 
                settings.EMAIL_HOST_USER, 
                [form.cleaned_data["email"]]
            )
            return redirect("goodBook")
    else:
        form = BookingForm()
    return render(request, "booking.html", {"form": form})

def goodBook(request):
    return render(request, "goodBook.html")


def contacts(request):
    return render(request, "contacts.html")

def detail_view (request, id):
    product = get_list_or_404(Product, id=id)
    photos = ProductImage.objects.filter(product=product)
    return render (request, "oneHotel.html",{
        'product':product,
        'photos':photos
    })





def comment(request, hotel_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post = get_object_or_404(Product, id=hotel_id)
            comment = Comment(
                name=comment_form.cleaned_data["name"],
                email=comment_form.cleaned_data["email"],
                body=comment_form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return render(request, "leaveComment.html")
    else:
        comment_form = CommentForm()
        return render(request, "comment.html", {"form": comment_form }) 

# def comment(request, oneHotel_id):
    # form = CommentForm(request.POST)
    # print("form", request)
    # print("idididid", oneHotel_id)
    # if request.method == "POST" and form.is_valid():
    #     new_comment = form.save(commit=False)
    #     new_comment.post = 2
    #     new_comment.save()
    #     print("111111")

        # a = Comment()
        # a.save()
        # new_comment = form.save(commit=False)
                
            #     # new_comment.product = product

            #     new_comment.save()
        # return redirect("leaveComment")
    # else:
    #     form = CommentForm()
#     return render(request, "comment.html", {"form": form})




def leaveComment(request):
    return render(request, "leaveComment.html")


def score(request, hotel_id):
    if request.method == "POST":
        score_form = ScoreForm(request.POST)
        if score_form.is_valid():
            post = get_object_or_404(Product, id=hotel_id)
            new_score = score_form.save(commit=False)
            new_score.post = post
            new_score.save()
            return render(request, "leaveScore.html")
    else:
        score_form = ScoreForm()
        return render(
            request,
            "score.html",
            {
                "form": score_form
            }
        )



