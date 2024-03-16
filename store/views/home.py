from store.models.category import Category
from store.models.product import Product
from django.views import View
from django.shortcuts import render

# def category_products(request,category_id):
#         category = Category.objects.get(pk=category_id)
#         products = Product.objects.filter(category=category)
#         return render(request, 'categories.html', {'categories': category, 'products': products})
class Home(View):
    def get(self,request):
        categories = Category.getAllCategory()
        return render(request,'home.html',{'categories':categories})
    def post():
        pass