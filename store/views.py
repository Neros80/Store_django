
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product": product})

