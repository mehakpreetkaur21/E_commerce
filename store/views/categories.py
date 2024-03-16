from store.models.category import Category
from store.models.product import Product
from django.views import View
from django.shortcuts import render

class Categories(View):
    def get(self,request):
        categories = Category.getAllCategory()
        return render(request,'categories.html',{'categories':categories})
    