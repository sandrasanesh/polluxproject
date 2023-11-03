from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from Frontend.models import contdb, regidb
from MyApp.models import catdb, productdb


# Create your views here.
def index_page(request):
    return render(request,"index.html")
def category_details(request):
    return render(request,"addcategory.html")
def savecat(request):
    if request.method=="POST":
        na=request.POST.get('cname')
        de=request.POST.get('des')
        img=request.FILES['cimg']
        obj=catdb(cname=na,des=de,cimg=img)
        obj.save()
        messages.success(request,"Category added successfully...")


        return redirect(category_details)
def display_category(request):
    cat=catdb.objects.all()
    return render(request,"displaycategory.html", {'cat': cat})
def edit_category(request,dataid):
    cat=catdb.objects.get(id=dataid)
    return render(request,"editcategory.html", {'cat': cat})
def update_category(request,dataid):
    if request.method == "POST":
        na = request.POST.get('cname')
        de = request.POST.get('des')
        try:
            img = request.FILES['cimg']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=catdb.objects.get(id=dataid).cimg
        catdb.objects.filter(id=dataid).update(cname=na,des=de,cimg=file)
        messages.success(request, "Category updated successfully...")
        return redirect(display_category)
def delete_cat(request,dataid):
    cat=catdb.objects.filter(id=dataid)
    cat.delete()
    messages.success(request, "Category deleted successfully...")
    return redirect(display_category)
def add_product(request):
    pro=catdb.objects.all()
    return render(request,"addproduct.html",{'pro':pro})
def savepro(request):
    if request.method=="POST":
        cna = request.POST.get('cname')

        na=request.POST.get('pname')
        de=request.POST.get('des')
        pr=request.POST.get('pri')
        img=request.FILES['pimg']
        obj=productdb(cname=cna,pname=na,des=de,pri=pr,pimg=img)
        obj.save()
        messages.success(request, "product added successfully...")
        return redirect(add_product)
def display_product(request):
    data=productdb.objects.all()
    return render(request,"displayproduct.html",{'data':data})
def edit_product(request,dataid):
    product=productdb.objects.get(id=dataid)
    return render(request,"editproduct.html",{'product': product})
def update_product(request,dataid):
    if request.method=="POST":
        cna = request.POST.get('cname')
        na = request.POST.get('pname')
        de = request.POST.get('des')
        pr = request.POST.get('pri')
        try:
            img = request.FILES['pimg']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).pimg
        productdb.objects.filter(id=dataid).update(cname=cna,pname=na,des=de,pri=pr,pimg=file)
        messages.success(request, "Category updated successfully...")
        return redirect(display_product)
def delete_product(request,dataid):
    product=productdb.objects.filter(id=dataid)
    product.delete()
    messages.success(request, "Category deleted successfully...")
    return redirect(display_product)
def login_page(request):
    return render(request,"AdminLogin.html")
def adminlogin(request):
    if request.method=="POST":
        un=request.POST.get('user_name')
        pwd=request.POST.get('pass_word')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(index_page)
            else:
                return redirect(login_page)
        else:
            return redirect(login_page)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)
def contact_us(request):
    data=contdb.objects.all()
    return render(request,"contactus.html",{'data':data})

def delete_contact(request,dataid):
    cont=contdb.objects.filter(id=dataid)
    cont.delete()
    return redirect(contact_us)
def registration_page(request):
    data=regidb.objects.all()
    return render(request,"registrationpage.html",{'data':data})







