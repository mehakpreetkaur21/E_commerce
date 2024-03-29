from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product

class Cart(View):
	def get(self,request):
		productList = list(request.session.get('cart').keys())
		if request.GET.get('increase'):
			pId = request.GET.get('increase')
			products = request.session.get('cart')
			products[pId] += 1
			request.session['cart'] = products

		if request.GET.get('decrease'):
			pId = request.GET.get('decrease')
			products = request.session.get('cart')
			if products[pId] > 1:
				products[pId] -= 1
				request.session['cart'] = products
				productList = list(request.session.get('cart').keys())
			else :
				del products[pId]
				request.session['cart'] = products
				productList = list(request.session.get('cart').keys())
		
		if request.GET.get('remove_item'):
			pId = request.GET.get('remove_item')
			products=request.session.get('cart')
			del products[pId]
			request.session['cart'] = products
			productList = list(request.session.get('cart').keys())
		if request.GET.get('clear_cart'):
			request.session['cart']={}

		allProduct = Product.getProductById(productList)
		return render(request,'cart.html',{"allProduct":allProduct})
	
	