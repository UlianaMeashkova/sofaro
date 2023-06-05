import logging
from django.core.cache import cache
from django.shortcuts import render

from django.db.models import Q
from products.models import Product

logger = logging.getLogger(__name__)


def index(request):
    title = request.GET.get("title")
    purchases__count = request.GET.get("purchases__count")

    result = cache.get(f"products-view-{title}-{purchases__count}-{request.user.id}")
    if result is not None:
        return result

    products = Product.objects.all()

    if title is not None:
        products = products.filter(title__icontains=title)

    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    response = render(request, "index.html", {"products": products})
    cache.set(f"products-view-{title}-{purchases__count}", response, 60 * 60)
    return response

def index(request):
    search = request.GET.get("search")

    products = Product.objects.all()

    if search is not None:
        products = products.filter(Q(title__icontains=search) | Q(description__icontains=search) | Q(price__icontains=search))

    # if purchases__count is not None:
    #     products = products.filter(purchases__count=purchases__count)

    response = render(request, "index.html", {"products": products})
   
    return response
# products = Product.objects.all()

# if title is not None:
#         products = products.filter(Q(title__icontains=title) | Q(description__icontains=title))

# if purchases__count is not None:
#         products = products.filter(purchases__count=purchases__count)

# response = render(request, "index.html", {"products": products})
# cache.set(f"products-view-{title}-{purchases__count}", response, 60 * 60)
#        return response
