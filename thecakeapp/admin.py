from django.contrib import admin
from .models import Orderer, Order, Store, Baker, Review, Option, DetailedOption, Cake

# Register your models here.

admin.site.register(Orderer)
admin.site.register(Baker)
admin.site.register(Store)
admin.site.register(Cake)
admin.site.register(DetailedOption)
admin.site.register(Order)
admin.site.register(Review)