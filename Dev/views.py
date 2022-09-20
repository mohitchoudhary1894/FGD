#import re
#from unicodedata import category
from os import remove
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.
def index(request): 
    if request.method=="POST":
        product_id=request.POST.get("cartid")
        remove=request.POST.get('minus')
        cart_dict=request.session.get('cart')
        
        if cart_dict:
            quantity = cart_dict.get(product_id)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart_dict.pop(product_id)
                    else:
                     cart_dict[product_id]=quantity-1
                else:
                 cart_dict[product_id]=quantity+1
            else:
                cart_dict[product_id] =1
        else:
             cart_dict={}
             cart_dict[product_id] = 1
       

             request.session['cart'] = cart_dict
        

    
         
    cate=Category.objects.all()
    c={}
    for i in cate:
        
        c.update({i.id:i.name})
        request.session['cate_name'] = c
    category_id=request.GET.get('cate_id')
    category_id=request.GET.get('cate_id')

     
    if 'search' in request.GET:     
        search = request.GET['search']
        try:
            categ= Category.objects.get(name=search)
            if categ:
                 products=product.objects.filter(Category=categ.id)
        except:
             products=product.objects.filter(product_name__icontains=search) 


    elif category_id:
        products=product.objects.filter(Category=category_id)
    else:
        products=product.objects.all()
       
    return render(request,'home.html',{'cat':cate,'pro':products})
def signup(request):
    if request.method=="POST":
        Fname=request.POST.get('first_name')
        Lname=request.POST.get('last_name')
        email_id=request.POST.get('email')
        password=request.POST.get('pwd')
        mobile=request.POST.get('mobile_no')
        gender=request.POST.get('gender')

        user_info=Registration(first_name=Fname,last_name=Lname,email=email_id,
        password= make_password(password),mobile=mobile,gender=gender)
       
        user_info.save()

    return HttpResponse("success")

def login(request):
    if request.method=="POST":
        error_msg= None
        email_id=request.POST.get('email')
        password=request.POST.get('psd')
        try:
            fetch_info=Registration.objects.get(email=email_id)
            if check_password(password,fetch_info.password):
                request.session['name']=fetch_info.first_name
                request.session['custome_id']=fetch_info.id
                request.session['email']=fetch_info.email
                return redirect('home')
            else:
                error_msg= "Password is Inccorect"
        except:
            error_msg= "Email is Not Register"
        return render(request,'home.html',{'error':error_msg})
        
def logout(request):
    request.session.clear()
    return redirect('home')

def cart_info(request):
    cart_item=request.session.get('cart').keys()
    filter_product=product.objects.filter(id__in=list(cart_item))
    return render(request,'cart.html',{'filter_product':filter_product})

def checkout(request):
    if request.method=="POST":
       
        address=request.POST.get('address')

        mobile=request.POST.get('mobile')
        customerid=request.session.get('custome_id')
        cart=request.session.get('cart')
        Product=product.objects.filter(id__in=list(cart.keys()))
        if not customerid:
             return HttpResponse("plz login")
            
        for pro in Product:
            save_order_dtls=order(address=address,mobile_no=mobile,product=pro,customer=Registration(id=customerid),
            quantity=cart.get(str(pro.id)),price=pro.price)
            save_order_dtls.save()
        request.session['cart']={}
        return redirect('cartdtls')
def Order_Dtls(request):
    customerid=request.session.get('custome_id')
    fetch_Order=order.objects.filter(customer=customerid)

    tp=0
    for i in fetch_Order:
        tp=tp+(i.price * i.quantity)
    return render(request,'order.html',{'fetch_dtls':fetch_Order,'tp':tp}) 

def text(request):
    products=product.objects.all()
    
    return render(request,'home.html',{'pro':products})