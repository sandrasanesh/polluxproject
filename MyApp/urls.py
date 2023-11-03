from django.urls import path
from MyApp import views
urlpatterns = [
    path('index_page/',views.index_page,name="index_page"),
    path('category_details/',views.category_details,name="category_details"),
    path('savecat/',views.savecat,name="savecat"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:dataid>/',views.edit_category,name="edit_category"),
    path('update_category/<int:dataid>/',views.update_category,name="update_category"),
    path('delete_cat/<int:dataid>/',views.delete_cat,name="delete_cat"),
    path('add_product/',views.add_product,name="add_product"),
    path('savepro/',views.savepro,name="savepro"),
    path('display_product/',views.display_product,name="display_product"),
    path('edit_product/<int:dataid>/',views.edit_product,name="edit_product"),
    path('update_product/<int:dataid>/',views.update_product,name="update_product"),
    path('delete_product/<int:dataid>/',views.delete_product,name="delete_product"),
    path('login_page/',views.login_page,name="login_page"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('contact_us/',views.contact_us,name="contact_us"),

    path('delete_contact/<int:dataid>',views.delete_contact,name="delete_contact"),
    path('registration_page/',views.registration_page,name="registration_page"),


]