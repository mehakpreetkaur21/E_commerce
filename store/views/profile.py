from django.shortcuts import render
from store.models.customer import Customer
def my_profile_view(request):
    customer=Customer.objects.get(id=request.session['customer'])
    print(customer)
    return render(request,'profile.html',{'customer':customer})


   