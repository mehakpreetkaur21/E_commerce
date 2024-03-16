from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order
from .models.wishlist import Wishlist

class AdminProduct(admin.ModelAdmin):
	list_display = ['id', 'name','price','category', 'date']


class AdminCategory(admin.ModelAdmin):
	list_display = ['id','name']



admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Wishlist)
