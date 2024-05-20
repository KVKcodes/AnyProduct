from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.contrib.auth import models, authenticate, login as auth_login, logout as auth_logout
from .models import Product_cart, Shopping_cart
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print("Welcome home soldier")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            print("Nope, you cant enter")
            return redirect('login')
    return render(request ,'login.html')

def signup(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        email= request.POST['email']
        password = request.POST['password']
        password1= request.POST['confirm_password']

        if password != password1:
            error_message="Passwords do not match!"
            print("error time")
            messages.error(request,error_message)
            return redirect('signup')
        if models.User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')
        
        if models.User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')
        
        if len(password) < 10:
            messages.error(request, "Pssh! Password is too weak!")
            return redirect('signup')

        user= models.User.objects.create_user(username= username, email= email, password= password)
        shopping_cart = Shopping_cart.objects.create(user= user)
        shopping_cart.save()

        auth_login(request, user)
        return redirect('home')
    return render(request ,'signup.html')

def contactus(request):
    return render(request ,'contacts.html')

def products(request):
    url= "https://freetestapi.com/api/v1/products"    
    response = requests.get(url)
    data = response.json()
    context = {'products': data}
    return render(request ,'products.html', context)

def product(request, id):
    url= f'https://freetestapi.com/api/v1/products/{id}'
    response = requests.get(url)
    data = response.json()
    context = {'product': data}
    return render(request ,'product.html', context)

@login_required(login_url='/login')
def shopping_cart(request):
    cart = Shopping_cart.objects.get(user=request.user)
    products = cart.product_list.all()
    subtotal= 0
    for product in products:
        subtotal+=product.price*product.quantity
    return render(request ,'shopping-cart.html', {'products': products, 'subtotal': subtotal})

@login_required(login_url='/login')
def add_cart(request):
    if request.method=="POST":
        cart = Shopping_cart.objects.get(user=request.user)
        size= request.POST['size']
        name= request.POST['product_name']
        price= request.POST['product_price']
        description= request.POST['product_description']
        quantity= request.POST['product_quantity']
        image_url= request.POST['product_image']
        brand= request.POST['product_brand']

        price = round(float(price), 2)
        quantity= int(quantity)

        product_cart = cart.product_list.filter(name=name, size=size).first()
        if product_cart:
            product_cart.quantity += quantity
            product_cart.save()
        else:
            product_cart = Product_cart.objects.create(
                cart=cart,
                size=size,
                name=name,
                price=price,
                description=description,
                quantity=quantity,
                image_link=image_url,
                brand=brand
            )
            cart.product_list.add(product_cart)


        alert_string= f'{quantity} {name} products have been added to your cart. Click here to check your cart'
        alert = {"alert_string": alert_string}

        url= "https://freetestapi.com/api/v1/products"    
        response = requests.get(url)
        data = response.json()
        context = {'products': data}
        context.update(alert)
        return render(request, 'products.html',  context)
    return render(request ,'shopping-cart.html')

def forgot_password(request):
    return render(request ,'forgot_password.html')

def forgot_password(request):
    return render(request ,'forgot_password.html')

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request) 
    return redirect('home')

def remove_cart(request):
    cart = Shopping_cart.objects.get(user=request.user)
    name = request.POST['product_name']
    size = request.POST['product_size']

    product= cart.product_list.get(name=name, size=size)
    product.delete()

    return redirect('shopping_cart')

def feedback(request):
    name = request.POST['name_contact']
    email = request.POST['email_contact']
    message = request.POST['message_contact']

    send_mail(
        f'Feed back from {name}',
        message,
        email,
        ["kvksiddartha@gmail.com"],
        fail_silently=False,    
    )

    response_message= f'We are AnyProduct.com.\nYour email has reached our inbox and we will get back to you as soon as we can!\nThank you for your patience :)\n\nRegards\nKVK Siddartha'
    send_mail(
        f'Hello {name}!',
        response_message,
        "kvksiddartha@gmail.com",
        [email],
        fail_silently=False,    
    )

    return redirect('shopping_cart')