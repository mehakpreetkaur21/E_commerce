from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from random import choice

def index(request):
    products = Product.getAllProduct().order_by('-id')
    product_list=[]
    while len(product_list)<12:
        item=choice(products)
        if item not in product_list:
                product_list.append(item)
        # product_list.append(choice(products))
    categories=list(Category.getAllCategory())
    customer=request.session.get('customer')
    if customer:
       customer_object=Customer.objects.get(id=request.session['customer'])
       return render(request,'index.html',{"products":product_list ,"categories":categories[-5:],"customer":customer_object})
    return render(request,'index.html',{"products":product_list ,"categories":categories[-5:]})

def category_index(request):
        categories = Category.getAllCategory()
        products = Product.getAllProduct().order_by('-id')
        product_list=[]
        for i in range(len(products)):
            item=choice(products)
            if item not in product_list:
                product_list.append(item)
        if request.GET.get('category_id'):
            filterProduct = Product.getProductByFilter(request.GET['category_id'])
            return render(request, 'index.html',{"products":filterProduct,"categories":categories})
        return render(request, 'index.html',{"products":product_list,"categories":categories})


