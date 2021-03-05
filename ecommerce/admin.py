from django.contrib import admin
from .models import Product , Cat
from .models import Contact , Order
# Register your models here.
admin.site.register(Product)
admin.site.register(Cat)
admin.site.register(Contact)
admin.site.register(Order)