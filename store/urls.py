from django.urls import path
from .views import Signup,Login,logout,Cart,Checkout,OrderView
from .views import Categories
from .views.index import index
from .views.products import about_us,search , Products
from .views.profile import my_profile_view
from .views.wishlist import Wishlist
from .middlewares import LoginCheckMiddleware,LogoutCheckMiddleware

urlpatterns = [
    path('products',Products.as_view(), name='products'),
    path('categories',Categories.as_view(),name='categories'),
    path('about_us',about_us,name='about_us'),
    path('search',search,name='search'),
    path('',index,name='index'),                                     
    path('profile',my_profile_view,name='my_profile_view'),
    path('signup',LogoutCheckMiddleware(Signup.as_view()), name='signup'),
    path('login',LogoutCheckMiddleware(Login.as_view()), name='login'),
    path('logout',LoginCheckMiddleware(logout), name='logout'),
    path('cart',Cart.as_view(), name='cart'),
    path('checkout',LoginCheckMiddleware(Checkout.as_view()), name='checkout'),
    path('order',LoginCheckMiddleware(OrderView.as_view()), name='order'),
    path('wishlist',LoginCheckMiddleware(Wishlist), name='wishlist'),
]
