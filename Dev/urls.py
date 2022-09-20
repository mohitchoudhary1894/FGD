from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('',views.index,name="home"),
   path('signup',views.signup,name="signup"),
   path('login',views.login,name="login"),
  path('logout',views.logout,name="logout"),
  path('cart',views.cart_info,name="cartdtls"),
  path('checkout',views.checkout,name="checkout"),
  path('order',views.Order_Dtls,name="order"),
  path('text',views.text,name="text"),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)