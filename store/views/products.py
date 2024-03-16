from django.shortcuts import render,redirect
from django.views import View
from store.models.product import Product
from store.models.category import Category
from random import choice
# from django.db.models import Q
class Products(View):

	def get(self,request):
		cart = request.session.get('cart')
		categories = Category.getAllCategory()
		products = Product.getAllProduct().order_by('-id')
		product_list=[]
		while (len(product_list)!=len(products)):
			item=choice(products)
			if item not in product_list:
				product_list.append(item)

		if request.GET.get('id'):
			filterProductById = Product.objects.get(id=int(request.GET.get('id')))
			return render(request, 'productDetail.html',{"product":filterProductById,"categories":categories})

		if not cart:
			request.session['cart'] = {}

		if request.GET.get('category_id'):
			filterProduct = Product.getProductByFilter(request.GET['category_id'])
			return render(request, 'products.html',{"products":filterProduct,"categories":categories})
		return render(request, 'products.html',{"products":product_list,"categories":categories})

	def post(self,request):
		product = request.POST.get('product')

		cart = request.session.get('cart')
		if cart:
			quantity = cart.get(product)
			if quantity:
				cart[product] = quantity+1
			else:
				cart[product] = 1
		else:
			cart = {}
			cart[product] = 1

		print(cart)
		request.session['cart'] = cart
		return redirect('cart')
	
def about_us(request):
	return render(request,'about_us.html')

def search(request):
    query = request.GET.get('query')
    search_product = Product.objects.filter(keyword__icontains=query)
    if search_product:
        return render(request, 'search.html', {"products": search_product ,"result":query})
    return render(request, 'search.html', {"products": None})



