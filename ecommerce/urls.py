from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='shop.home'),
    path('about',views.about,name='shop.about'),
    path('contact',views.contact,name='shop.contact'),
    path('tracker',views.tracker,name = 'shop.tracker'),
    path('search', views.search,name= 'shop.search'),
    path('checkout',views.checkout,name = 'shop.checkout'),
    path('products/<int:myid>', views.product, name = 'shop.product')
]
