from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
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


def products_detail_view(request):
    objs = Product.objects.all()
    context = {'objects': objs, 'additional_time': request.additional_time}
    print(f'dir(request): {dir(request)}')
    # print(f'COOKIES: {request.COOKIES}')
    # print(f'META: {request.META}')
    return render(request, 'products/details.html', context)


def product_detail_view(request, _id):
    # obj = Product.objects.get(id=_id)
    obj = get_object_or_404(Product, id=_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/products')
    context = {'obj': obj}
    return render(request, 'products/detail.html', context)
