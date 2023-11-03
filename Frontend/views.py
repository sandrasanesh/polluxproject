from django.contrib import messages
from django.shortcuts import render, redirect

from Frontend.models import contdb, regidb, cartdb
from MyApp.models import catdb, productdb


# Create your views here.
def homepage(request):
    cat=catdb.objects.all()
    return render(request,"Home.html",{'cat':cat})
def product_page(request):
    product=productdb.objects.all()
    return render(request,"products.html",{'product':product})
def category_page(request,cat_name):
    data=productdb.objects.filter(cname=cat_name)
    return render(request,"category.html",{'data':data})
def single_product(request,proid):
    data=productdb.objects.get(id=proid)
    return render(request,"singleproduct.html",{'data':data})
def about_us(request):
    return render(request,"aboutus.html")
def services_page(request):
    return render(request,"services.html")
def contact_page(request):
    return render(request,"contact_page.html")
def savecontact(request):
    if request.method=="POST":
        fn=request.POST.get('firstname')
        ln=request.POST.get('lastname')
        mail=request.POST.get('email')
        phn=request.POST.get('phone')
        obj=contdb(firstname=fn,lastname=ln,email=mail,phone=phn)
        obj.save()
        return redirect(contact_page)
def userlogin(request):
    return render(request,"userlogin.html")
def signin(request):
    return render(request,"signup.html")
def reg_page(request):
    if request.method=="POST":
        na=request.POST.get('name')
        mob=request.POST.get('mob')
        mail=request.POST.get('email')
        uname=request.POST.get('username')
        pas=request.POST.get('password')
        repas=request.POST.get('re_password')
        obj=regidb(name=na,mob=mob,email=mail,username=uname,password=pas,re_password=repas)
        obj.save()
        return redirect(signin)
def userlog(request):
    if request.method=="POST":
        un=request.POST.get('name')
        pwd=request.POST.get('password')
        if regidb.objects.filter(name=un,password=pwd).exists():
            request.session['name']=un
            request.session['password']=pwd
            messages.success(request, "user logged successfully...")
            return redirect(homepage)
        else:
            messages.error(request, "invalid user...")
            return redirect(userlogin)
    else:
        messages.error(request, "invalid user...")
        return redirect(userlogin)
def user_logout(request):
    del request.session['name']
    del request.session['password']
    return redirect(userlogin)
def cart_page(request):
    data=cartdb.objects.filter(username=request.session['name'])
    total_price=0
    for i in data:
        total_price=total_price+i.total_price
    return render(request,"cartpage.html",{'data':data,'total_price':total_price})
def savecart(request):
    if request.method=="POST":
        qua=request.POST.get('qty')
        name=request.POST.get('username')
        pname=request.POST.get('productname')
        descr=request.POST.get('des')
        total=request.POST.get('total_price')
        obj=cartdb(qty=qua,username=name,productname=pname,des=descr,total_price=total)
        obj.save()
        messages.success(request, "product added to cart successfully...")
        return redirect('cart_page')
def delcart(request,dataid):
    data=cartdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "product deleted from cart successfully...")
    return redirect(cart_page)
def checkout(request):
    data=cartdb.objects.filter(username=request.session['name'])
    total_price=0
    for i in data:
        total_price = total_price + i.total_price
        messages.success(request, "congrats..your order is placed")
    return render(request,"checkout.html",{'data':data,'total_price':total_price})




