from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.core.mail import send_mail

class Login(View):
	return_url = None
	def get(self,request):
		Login.return_url = request.GET.get('return_url')
		return render(request,'login.html')

	def post(self,request):
		userData = request.POST
		customerEmail = Customer.emailExits(userData["email"])
		# print(send_mail("Test", "test", "komalmehak823@gmail.com", ["kmehakpreet001@gmail.com"],fail_silently=False))
		print(customerEmail)
		if customerEmail:
			if check_password(userData["password"],customerEmail.password):
				request.session["customer"] = customerEmail.id
				if Login.return_url:
					return HttpResponseRedirect(Login.return_url)
				else:
					Login.return_url = None
					return redirect('index')
			else:
				return render(request,'login.html',{"userData":userData,"error":"Email or password doesn't match"})
		else:
			return render(request,'login.html',{"userData":userData,"error":"Email or password doesn't match"})

def logout(request):
	request.session.clear()
	return redirect('index')