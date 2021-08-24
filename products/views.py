from django.shortcuts import render

from .forms import ProductForm
from .models import Product


def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {'form': form}
    return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    objs = Product.objects.all()
    context = {'objects': objs}
    return render(request, 'products/detail.html', context)
