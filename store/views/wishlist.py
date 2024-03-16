from django.shortcuts import render, redirect
from store.models.customer import Customer
from store.models.wishlist import Wishlist

def Wishlist(request):
    # wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': ""})

def add_to_wishlist(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        if product_name:
            Wishlist.objects.create(user=request.user, product_name=product_name)
            return redirect('wishlist')

    return render(request, 'add_to_wishlist.html')

def remove_from_wishlist(request, item_id):
    wishlist_item = Wishlist.objects.get(id=item_id)
    if wishlist_item.user == request.user:
        wishlist_item.delete()
    return redirect('wishlist')