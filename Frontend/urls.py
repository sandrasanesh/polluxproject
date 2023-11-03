from django.urls import path
from Frontend import views

urlpatterns=[
     path('homepage/',views.homepage,name="homepage"),
     path('product_page/',views.product_page,name="product_page"),
     path('category_page/<cat_name>/',views.category_page,name="category_page"),
     path('single_product/<int:proid>',views.single_product,name="single_product"),
     path('about_us',views.about_us,name="about_us"),
     path('services_page',views.services_page,name="services_page"),
     path('contact_page',views.contact_page,name="contact_page"),
     path('savecontact/',views.savecontact,name="savecontact"),
     path('userlogin/',views.userlogin,name="userlogin"),
     path('signin/',views.signin,name="signin"),
     path('reg_page/',views.reg_page,name="reg_page"),
     path('userlog/',views.userlog,name="userlog"),
     path('user_logout/',views.user_logout,name="user_logout"),
     path('cart_page/',views.cart_page,name="cart_page"),
     path('savecart/',views.savecart,name="savecart"),
     path('delcart/<int:dataid>/',views.delcart,name="delcart"),
     path('checkout/',views.checkout,name="checkout"),
 ]