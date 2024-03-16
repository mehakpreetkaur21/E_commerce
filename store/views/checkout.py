from django.shortcuts import render, redirect
from django.views import View
from store.models.order import Order
from store.models.customer import Customer
from store.models.product import Product


class Checkout(View):
	def get(self,request):
		return render (request,'checkout.html')
		# return redirect('cart')
	
	def post(self,request):
		cart = request.session.get('cart')
		address = request.POST.get('address')
		phone = request.POST.get('phone')
		products = Product.getProductById(list(cart.keys()))
		customer = request.session.get('customer')
		print(address,phone,cart,products,customer)

		for product in products:
			newOrder = Order(
					product=product,
					customer=Customer(id=customer),
					quantity=cart[str(product.id)],
					price=product.price,
					address=address,
					phone=phone,

				)
			newOrder.save()

		request.session['cart'] = {}
		return redirect('order')
