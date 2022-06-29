"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('mindex/', views.mindex, name='mindex'),
    path('cart/', views.cart, name='cart'),
    path('categories/', views.categories, name='categories'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('loginevaluate/', views.loginevaluate, name='loginevaluate'),
    path('registrationpage/', views.registrationpage, name='registrationpage'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('resetpassword/', views.resetpassword, name='resetpassword'),
    path('sendotp/', views.sendotp, name='sendotp'),

    path('addproduct/', views.addproduct, name='addproduct'),
    path('updateproduct/', views.updateproduct, name='updateproduct'),
    path('editproduct/<int:pk>', views.editproduct, name='editproduct'),
    path('deleteproduct/<int:pk>', views.deleteproduct, name='deleteproduct'),
    path('allproducts/', views.allproducts, name='allproducts'),
    path('viewproduct/<int:pk>', views.viewproduct, name='viewproduct'),
    path('savechanges/', views.savechanges, name='savechanges'),



    path('review/', views.review, name='review'),
    path('viewreviews/', views.viewreviews, name='viewreviews'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('deletecartproduct/<int:pk>', views.deletecartproduct, name='deletecartproduct'),
    path('clearcart/', views.clearcart, name='clearcart'),
    path('postmessage/', views.postmessage, name='postmessage'),

    path('allmessages/', views.allmessages, name='allmessages'),
    path('myprofile/', views.myprofile, name='myprofile'),

    path('editprofile/', views.editprofile, name='editprofile'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('allsubscribers/', views.allsubscribers, name='allsubscribers'),
    path('deletesubscriber/<int:pk>', views.deletesubscriber, name='deletesubscriber'),
    path('subscribed/', views.subscribed, name='subscribed'),

    path('pushmessage/', views.pushmessage, name='pushmessage'),

    path('addtowishlist/<int:pk>', views.addtowishlist, name='addtowishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('removefromwishlist/<int:pk>', views.removefromwishlist, name='removefromwishlist'),

    path('addcoupon/', views.addcoupon, name='addcoupon'),
    path('allcoupon/', views.allcoupon, name='allcoupon'),
    path('updatecoupon/', views.updatecoupon, name='updatecoupon'),
    path('deletecoupon/<int:pk>', views.deletecoupon, name='deletecoupon'),

    path('applycoupon/', views.applycoupon, name='applycoupon'),
    path('removecoupon/', views.removecoupon, name='removecoupon'),

    path('savebilling/', views.savebilling, name='savebilling'),
    path('placeorder/', views.placeorder, name='placeorder'),
    path('orderplaced/', views.orderplaced, name='orderplaced'),
    path('myorders/', views.myorders, name='myorders'),
    path('allorders/', views.allorders, name='allorders'),
    path('editorderstatus/', views.editorderstatus, name='editorderstatus'),

]
