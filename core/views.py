from django.shortcuts import render

# Create your views here.
from store.models import Product


def frontpage(request):
    products = Product.objects.all().filter(is_featured=True)
    context = {'products': products}
    return render(request, 'frontpage.html', context)


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
