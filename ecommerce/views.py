from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order
from math import ceil


# Create your views here.
def index(request):
    products = Product.objects.all()
    # n = len(products)
    # slides = n // 4 + ceil((n / 4) - (n // 4))
    # content = {
    #     'no of slide': slides,
    #     'product': products,
    #     'range': range(1, slides)
    #
    # }
    # only use  to create multiple or we can say two slide
    # allproducts = [[products,range(1,slides),slides],[products,range(1,slides),slides]]

    # for slidewise category we have to import catogory from database
    allproducts = []
    category = Product.objects.values('category', 'id')
    cat = {item['category'] for item in category}
    for cats in cat:
        prod = Product.objects.filter(category=cats)
        n = len(prod)
        slides = n // 4 + ceil((n / 4) - (n // 4))

        allproducts.append([prod, range(1, slides), slides])

    content = {
        'allproducts': allproducts
    }
    return render(request, 'shop/index1.html', content)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        area = request.POST.get('area', '')
        contact = Contact(email=email, password=password, area=area)
        contact.save()

    return render(request, 'shop/contact.html')


def search(request):
    return render(request, 'shop/search.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def checkout(request):
    if request.method == 'POST':
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(name=name, email=email, phone=phone, address=address, city=city, zip_code=zip_code,
                      itemsJson=itemsJson)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')


def product(request, myid):
    product = Product.objects.filter(id=myid)
    pro = {
        'product': product[0]
    }
    return render(request, 'shop/productview.html', pro)
