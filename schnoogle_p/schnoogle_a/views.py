from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.core.files import File
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.urls import reverse
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from django.views.decorators.http import require_POST

# Create your views here.

def newsletter_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')  # get the value of the name field, default to an empty string if not present
        email = request.POST['email']
        newsletter = Newsletter(name=name, email=email)
        newsletter.save()
        # do something with the new newsletter object, like sending a confirmation email
        return render(request, 'schnoogle_a/store.html')

def privacy(request):
    current_date = datetime.now()
    context = {'current_date': current_date}
    return render(request, 'schnoogle_a/privacy.html', context)

def about(request):
    return render(request, 'schnoogle_a/about.html')

def feedback(request):
    if request.method == 'POST':
        feedback=Feedback()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message',)
        feedback.name=name
        feedback.email=email
        feedback.subject=subject
        feedback.message=message
        feedback.save()
       
        return HttpResponse("<h1>THANK YOU</h1>")
    
    return render(request, 'schnoogle_a/feedback.html')

def store(request):
    if request.user.is_authenticated:
        login_label = 'Log out'
    else:
        login_label = 'Log in'

    context = {
        'login_label': login_label
    }
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'schnoogle_a/store.html', context)




def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zip')
        cardname = request.POST.get('cardname')
        cardnumber = request.POST.get('cardnumber')
        expmonth = request.POST.get('expmonth')
        expyear = request.POST.get('expyear')
        cvv = request.POST.get('cvv')

        # Create order
        order = Order.objects.create(customer=request.user.customer, date_ordered=datetime.now())

        # Save shipping address to the database
        shipping_address = ShippingAddress(customer=request.user.customer, 
                                            order=order,
                                            address=address, 
                                            city=city, 
                                            state=state, 
                                            zipcode=zipcode)
        shipping_address.save()

        return redirect('feedback')
    else:
        return render(request, 'schnoogle_a/checkout.html')



@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'schnoogle_a/cart_detail.html')

def toys(request):
    product1 = Products() 
    product1.id = 13
    product1.name = 'Wooden kitchen set'
    product1.price = 1100
    image1 = 'static/images/kitchenset2.jpg'

    # Open the image file and create an ImageField object
    print(image1)
    with open(image1, 'rb') as f:
     product1.image.save('kitchenset2.jpg', File(f), save=True)

    product2 = Products() 
    product2.id = 14
    product2.name = 'Multicolor plastic set'
    product2.price = 1600
    image2 = 'static/images/kitchenset1.jpg'

    # Open the image file and create an ImageField object
    print(image2)
    with open(image2, 'rb') as f:
     product2.image.save('kitchenset1.jpg', File(f), save=True)

    product3 = Products() 
    product3.id = 15
    product3.name = 'Mini market'
    product3.price = 400
    image3 = 'static/images/kitchenset3.jpg'

    # Open the image file and create an ImageField object
    print(image3)
    with open(image3, 'rb') as f:
     product3.image.save('kitchenset3.jpg', File(f), save=True)

    product4 = Products() 
    product4.id = 35
    product4.name = 'Giant Roller'
    product4.price = 399
    image4 = 'static/images/outdoor1.jpg'

    # Open the image file and create an ImageField object
    print(image4)
    with open(image4, 'rb') as f:
     product4.image.save('outdoor1.jpg', File(f), save=True)

    product5 = Products() 
    product5.id = 36
    product5.name = 'Dragonfly flying stick'
    product5.price = 850
    image5 = 'static/images/outdoor2.jpg'

    # Open the image file and create an ImageField object
    print(image5)
    with open(image5, 'rb') as f:
     product5.image.save('outdoor2.jpg', File(f), save=True)

    product6 = Products() 
    product6.id = 37
    product6.name = 'Disney Princess Carriage'
    product6.price = 390
    image6 = 'static/images/outdoor3.jpg'

    # Open the image file and create an ImageField object
    print(image6)
    with open(image6, 'rb') as f:
     product6.image.save('outdoor3.jpg', File(f), save=True)

    product7 = Products() 
    product7.id = 9
    product7.name = 'Rare bears soft plushy'
    product7.price = 799
    image7 = 'static/images/bs13.jpg'

    # Open the image file and create an ImageField object
    print(image7)
    with open(image7, 'rb') as f:
     product7.image.save('bs13.jpg', File(f), save=True)

    product8 = Products() 
    product8.id = 10
    product8.name = 'Japanese sushi rice cushion plushy'
    product8.price = 9799
    image8 = 'static/images/bs14.jpg'

    # Open the image file and create an ImageField object
    print(image8)
    with open(image8, 'rb') as f:
     product8.image.save('bs14.jpg', File(f), save=True)

    product9 = Products() 
    product9.id = 11
    product9.name = 'Unicorn soft plushy'
    product9.price = 3499
    image9 = 'static/images/bs18.jpg'

    # Open the image file and create an ImageField object
    print(image9)
    with open(image9, 'rb') as f:
     product9.image.save('bs18.jpg', File(f), save=True)

    product10 = Products() 
    product10.id = 20
    product10.name = 'Wooden alphabet board'
    product10.price = 799
    image10 = 'static/images/edu1.jpg'

    # Open the image file and create an ImageField object
    print(image10)
    with open(image10, 'rb') as f:
     product10.image.save('edu1.jpg', File(f), save=True)

    product11 = Products() 
    product11.id = 21
    product11.name = 'Wooden puzzle board'
    product11.price = 1399
    image11 = 'static/images/edu2.jpg'

    # Open the image file and create an ImageField object
    print(image11)
    with open(image11, 'rb') as f:
     product11.image.save('edu2.jpg', File(f), save=True)

    product12 = Products() 
    product12.id = 22
    product12.name = 'Wooden number board'
    product12.price = 820
    image12 = 'static/images/edu3.jpg'

    # Open the image file and create an ImageField object
    print(image12)
    with open(image12, 'rb') as f:
     product12.image.save('edu3.jpg', File(f), save=True)

     products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12]

    return render(request, 'schnoogle_a/toys.html', {'products': products})


def diapering(request):
    product13 = Products() 
    product13.id = 26
    product13.name = 'Baby massage oil'
    product13.price = 400
    image13 = 'static/images/skincare.jpg'

    # Open the image file and create an ImageField object
    print(image13)
    with open(image13, 'rb') as f:
     product13.image.save('skincare.jpg', File(f), save=True)

    product14 = Products() 
    product14.id = 27
    product14.name = 'Baby lotion'
    product14.price = 850
    image14 = 'static/images/skincare2.jpg'

    # Open the image file and create an ImageField object
    print(image14)
    with open(image14, 'rb') as f:
     product14.image.save('skincare2.jpg', File(f), save=True)

    product15 = Products() 
    product15.id = 28
    product15.name = 'Baby powder'
    product15.price = 390
    image15 = 'static/images/skincare3.jpg'

    # Open the image file and create an ImageField object
    print(image15)
    with open(image15, 'rb') as f:
     product15.image.save('skincare3.jpg', File(f), save=True)

    product16 = Products() 
    product16.id = 29
    product16.name = 'Bathroom kit'
    product16.price = 4599
    image16 = 'static/images/tt1.jpg'

    # Open the image file and create an ImageField object
    print(image16)
    with open(image16, 'rb') as f:
     product16.image.save('tt1.jpg', File(f), save=True)

    product17 = Products() 
    product17.id = 30
    product17.name = 'Baby shampoo'
    product17.price = 9799
    image17 = 'static/images/tt2.jpg'

    # Open the image file and create an ImageField object
    print(image17)
    with open(image17, 'rb') as f:
     product17.image.save('tt2.jpg', File(f), save=True)

    product18 = Products() 
    product18.id = 31
    product18.name = 'Body wash'
    product18.price = 3499
    image18 = 'static/images/tt3.jpg'

    # Open the image file and create an ImageField object
    print(image18)
    with open(image18, 'rb') as f:
     product18.image.save('tt3.jpg', File(f), save=True)

    product19 = Products() 
    product19.id = 32
    product19.name = 'Pot'
    product19.price = 799
    image19 = 'static/images/OE1.jpg'

    # Open the image file and create an ImageField object
    print(image19)
    with open(image19, 'rb') as f:
     product19.image.save('OE1.jpg', File(f), save=True)

    product20 = Products() 
    product20.id = 33
    product20.name = 'Nappies'
    product20.price = 1399
    image20 = 'static/images/OE2.jpg'

    # Open the image file and create an ImageField object
    print(image20)
    with open(image20, 'rb') as f:
     product20.image.save('OE2.jpg', File(f), save=True)

    product21 = Products() 
    product21.id = 34
    product21.name = 'Wipes'
    product21.price = 820
    image21 = 'static/images/OE3.jpg'

    # Open the image file and create an ImageField object
    print(image21)
    with open(image21, 'rb') as f:
     product21.image.save('OE3.jpg', File(f), save=True)

    product22 = Products() 
    product22.id = 23
    product22.name = 'Huggies'
    product22.price = 1100
    image22 = 'static/images/diapers.jpg'

    # Open the image file and create an ImageField object
    print(image22)
    with open(image22, 'rb') as f:
     product22.image.save('diapers.jpg', File(f), save=True)

    product23 = Products() 
    product23.id = 24
    product23.name = 'Pampers'
    product23.price = 160
    image23 = 'static/images/diaper2.jpg'

    # Open the image file and create an ImageField object
    print(image23)
    with open(image23, 'rb') as f:
     product23.image.save('diaper2.jpg', File(f), save=True)

    product24 = Products() 
    product24.id = 25
    product24.name = 'Many poko pants'
    product24.price = 400
    image24 = 'static/images/diaper3.jpg'

    # Open the image file and create an ImageField object
    print(image24)
    with open(image24, 'rb') as f:
     product24.image.save('diaper3.jpg', File(f), save=True)

     products = [product13, product14, product15, product16, product17, product18, product19, product20, product21, product22, product23, product24]

    return render(request, 'schnoogle_a/diapering.html', {'products': products})

def tshirtsB(request):
    product25 = Products() 
    product25.id = 38
    product25.name = 'Super hero dad'
    product25.price = 1000
    image25 = 'static/images/tb4.jpg'

    # Open the image file and create an ImageField object
    print(image25)
    with open(image25, 'rb') as f:
     product25.image.save('tb4.jpg', File(f), save=True)

    product26 = Products() 
    product26.id = 39
    product26.name = 'Cute panda t-shirt'
    product26.price = 560
    image26 = 'static/images/tb5.jpg'

    # Open the image file and create an ImageField object
    print(image26)
    with open(image26, 'rb') as f:
     product26.image.save('tb5.jpg', File(f), save=True)

    product27 = Products() 
    product27.id = 40
    product27.name = 'Baby boss t-shirt'
    product27.price = 500
    image27 = 'static/images/tb6.jpg'

    # Open the image file and create an ImageField object
    print(image27)
    with open(image27, 'rb') as f:
     product27.image.save('tb6.jpg', File(f), save=True)

    product28 = Products() 
    product28.id = 41
    product28.name = 'Black printed t-shirt'
    product28.price = 400
    image28 = 'static/images/tb1.jpg'

    # Open the image file and create an ImageField object
    print(image28)
    with open(image28, 'rb') as f:
     product28.image.save('tb1.jpg', File(f), save=True)

    product29 = Products() 
    product29.id = 42
    product29.name = 'Pure cotton tshirt'
    product29.price = 850
    image29= 'static/images/tb2.jpg'

    # Open the image file and create an ImageField object
    print(image29)
    with open(image29, 'rb') as f:
     product29.image.save('tb2.jpg', File(f), save=True)

    product30 = Products() 
    product30.id = 43
    product30.name = 'White printed tshirt'
    product30.price = 390
    image30 = 'static/images/tb3.jpg'

    # Open the image file and create an ImageField object
    print(image30)
    with open(image30, 'rb') as f:
     product30.image.save('tb3.jpg', File(f), save=True)

    product31 = Products() 
    product31.id = 44
    product31.name = 'Cool tshirt'
    product31.price = 459
    image31 = 'static/images/tb7.jpg'

    # Open the image file and create an ImageField object
    print(image31)
    with open(image31, 'rb') as f:
     product31.image.save('tb7.jpg', File(f), save=True)

    product32 = Products() 
    product32.id = 45
    product32.name = 'Long sleeve Tshirt'
    product32.price = 799
    image32 = 'static/images/tb8.jpg'

    # Open the image file and create an ImageField object
    print(image32)
    with open(image32, 'rb') as f:
     product32.image.save('tb8.jpg', File(f), save=True)

    product33 = Products() 
    product33.id = 46
    product33.name = 'Be great T-shirt'
    product33.price = 499
    image33 = 'static/images/tb9.png'

    # Open the image file and create an ImageField object
    print(image33)
    with open(image33, 'rb') as f:
     product33.image.save('tb9.png', File(f), save=True)

    product34 = Products() 
    product34.id = 47
    product34.name = 'White Shirt'
    product34.price = 799
    image34 = 'static/images/tb10.jpg'

    # Open the image file and create an ImageField object
    print(image34)
    with open(image34, 'rb') as f:
     product34.image.save('tb10.jpg', File(f), save=True)

    product35 = Products() 
    product35.id = 48
    product35.name = 'Blue stripes shirt'
    product35.price = 899
    image35 = 'static/images/tb11.jpg'

    # Open the image file and create an ImageField object
    print(image35)
    with open(image35, 'rb') as f:
     product35.image.save('tb11.jpg', File(f), save=True)

    product36 = Products() 
    product36.id = 49
    product36.name = 'Green stripes shirt'
    product36.price = 759
    image36 = 'static/images/tb12.jpg'

    # Open the image file and create an ImageField object
    print(image36)
    with open(image36, 'rb') as f:
     product36.image.save('tb12.jpg', File(f), save=True)

     products = [product25, product26, product27, product28, product29, product30, product31, product32, product33, product34, product35, product36]

    return render(request, 'schnoogle_a/toys.html', {'products': products})

def footwearB(request):
    product37 = Products() 
    product37.id = 50
    product37.name = 'Leather boots'
    product37.price = 1100
    image37 = 'static/images/shoes1.jpg'

    # Open the image file and create an ImageField object
    print(image37)
    with open(image37, 'rb') as f:
     product37.image.save('shoes1.jpg', File(f), save=True)

    product38 = Products() 
    product38.id = 51
    product38.name = 'Sneakers'
    product38.price = 1160
    image38 = 'static/images/shoes2.jpg'

    # Open the image file and create an ImageField object
    print(image38)
    with open(image38, 'rb') as f:
     product38.image.save('shoes2.jpg', File(f), save=True)

    product39 = Products() 
    product39.id = 52
    product39.name = 'Sport shoes'
    product39.price = 400
    image39 = 'static/images/shoes3.jpg'

    # Open the image file and create an ImageField object
    print(image39)
    with open(image39, 'rb') as f:
     product39.image.save('shoes3.jpg', File(f), save=True)

    product40 = Products() 
    product40.id = 53
    product40.name = 'LED sandals'
    product40.price = 700
    image40 = 'static/images/sanb1.jpg'

    # Open the image file and create an ImageField object
    print(image40)
    with open(image40, 'rb') as f:
     product40.image.save('sanb1.jpg', File(f), save=True)

    product41 = Products() 
    product41.id = 54
    product41.name = 'Double buckle sandal'
    product41.price = 950
    image41 = 'static/images/sanb2.jpg'

    # Open the image file and create an ImageField object
    print(image41)
    with open(image41, 'rb') as f:
     product41.image.save('sanb2.jpg', File(f), save=True)

    product42 = Products() 
    product42.id = 55
    product42.name = ' Rubber sandals'
    product42.price = 500
    image42 = 'static/images/sanb3.jpg'

    # Open the image file and create an ImageField object
    print(image42)
    with open(image42, 'rb') as f:
     product42.image.save('sanb3.jpg', File(f), save=True)

    product43 = Products() 
    product43.id = 56
    product43.name = 'Cute booties'
    product43.price = 300
    image43 = 'static/images/sob.1.jpg'

    # Open the image file and create an ImageField object
    print(image43)
    with open(image43, 'rb') as f:
     product43.image.save('sob.1.jpg', File(f), save=True)

    product44 = Products() 
    product44.id = 57
    product44.name = 'Crochet pattern socks'
    product44.price = 359
    image44 = 'static/images/sob2.jpg'

    # Open the image file and create an ImageField object
    print(image44)
    with open(image44, 'rb') as f:
     product44.image.save('sob2.jpg', File(f), save=True)

    product45 = Products() 
    product45.id = 58
    product45.name = 'Ankle lenth socks'
    product45.price = 99
    image45 = 'static/images/sob3.jpg'

    # Open the image file and create an ImageField object
    print(image45)
    with open(image45, 'rb') as f:
     product45.image.save('sob3.jpg', File(f), save=True)

    product46 = Products() 
    product46.id = 59
    product46.name = 'Shrek crocs'
    product46.price = 899
    image46 = 'static/images/crocsB1.jpg'

    # Open the image file and create an ImageField object
    print(image46)
    with open(image46, 'rb') as f:
     product46.image.save('crocsB1.jpg', File(f), save=True)

    product47 = Products() 
    product47.id = 60
    product47.name = 'Dog shaped crocs'
    product47.price = 799
    image47 = 'static/images/croccB3.jpg'

    # Open the image file and create an ImageField object
    print(image47)
    with open(image47, 'rb') as f:
     product47.image.save('croccB3.jpg', File(f), save=True)

    product48 = Products() 
    product48.id = 61
    product48.name = 'Cow print crocs'
    product48.price = 1299
    image48 = 'static/images/crocsB3.jpg'

    # Open the image file and create an ImageField object
    print(image48)
    with open(image48, 'rb') as f:
     product48.image.save('crocsB3.jpg', File(f), save=True)

     products = [product37, product38, product39, product40, product41, product42, product43, product44, product45, product46, product47, product48]

    return render(request, 'schnoogle_a/footwearB.html', {'products': products})

def winterB(request):
    product49 = Products() 
    product49.id = 62
    product49.name = 'Pink knit jumpsuit'
    product49.price = 2000
    image49 = 'static/images/winterset1.jpg'

    # Open the image file and create an ImageField object
    print(image49)
    with open(image49, 'rb') as f:
     product49.image.save('winterset1.jpg', File(f), save=True)

    product50 = Products() 
    product50.id = 63
    product50.name = 'Hooded jumpsuit'
    product50.price = 1560
    image50 = 'static/images/winterset2.jpg'

    # Open the image file and create an ImageField object
    print(image50)
    with open(image50, 'rb') as f:
     product50.image.save('winterset2.jpg', File(f), save=True)

    product51 = Products() 
    product51.id = 64
    product51.name = 'Cute bear jumpsuit'
    product51.price = 1460
    image51 = 'static/images/bs22.jpg'

    # Open the image file and create an ImageField object
    print(image51)
    with open(image51, 'rb') as f:
     product51.image.save('bs22.jpg', File(f), save=True)

    product52 = Products() 
    product52.id = 65
    product52.name = 'Brown woolen cap'
    product52.price = 1500
    image52 = 'static/images/wintercaps1.jpg'

    # Open the image file and create an ImageField object
    print(image52)
    with open(image52, 'rb') as f:
     product52.image.save('wintercaps1.jpg', File(f), save=True)

    product53 = Products() 
    product53.id = 66
    product53.name = 'Beanie Cap'
    product53.price = 450
    image53 = 'static/images/wintercaps2.jpg'

    # Open the image file and create an ImageField object
    print(image53)
    with open(image53, 'rb') as f:
     product53.image.save('wintercaps2.jpg', File(f), save=True)

    product54 = Products() 
    product54.id = 67
    product54.name = ' Grey cap and gloves set'
    product54.price = 390
    image54 = 'static/images/wintercaps3.jpg'

    # Open the image file and create an ImageField object
    print(image54)
    with open(image54, 'rb') as f:
     product54.image.save('wintercaps3.jpg', File(f), save=True)

    product55 = Products() 
    product55.id = 68
    product55.name = 'Sweatsuit'
    product55.price = 499
    image55 = 'static/images/winterset2.jpg'

    # Open the image file and create an ImageField object
    print(image55)
    with open(image55, 'rb') as f:
     product55.image.save('winterset2.jpg', File(f), save=True)

    product56 = Products() 
    product56.id = 69
    product56.name = 'Flannel Animal Jumpsuit'
    product56.price = 999
    image56 = 'static/images/winterset4.jpg'

    # Open the image file and create an ImageField object
    print(image56)
    with open(image56, 'rb') as f:
     product56.image.save('winterset4.jpg', File(f), save=True)

    product57 = Products() 
    product57.id = 70
    product57.name = 'Plaid duffle coat'
    product57.price = 1499
    image57 = 'static/images/winterset5.jpg'

    # Open the image file and create an ImageField object
    print(image57)
    with open(image57, 'rb') as f:
     product57.image.save('winterset5.jpg', File(f), save=True)

    product58 = Products() 
    product58.id = 71
    product58.name = 'Beige fur hoodie'
    product58.price = 899
    image58 = 'static/images/hood3.jpg'

    # Open the image file and create an ImageField object
    print(image58)
    with open(image58, 'rb') as f:
     product58.image.save('hood3.jpg', File(f), save=True)

    product59 = Products() 
    product59.id = 72
    product59.name = 'Black and grey fur hoodie'
    product59.price = 799
    image59 = 'static/images/hood2.jpg'

    # Open the image file and create an ImageField object
    print(image59)
    with open(image59, 'rb') as f:
     product59.image.save('croccB3.jpg', File(f), save=True)

    product60 = Products() 
    product60.id = 73
    product60.name = 'Panda print hoodie'
    product60.price = 799
    image60 = 'static/images/hood1.jpg'

    # Open the image file and create an ImageField object
    print(image60)
    with open(image60, 'rb') as f:
     product60.image.save('crocsB3.jpg', File(f), save=True)

     products = [product49, product50, product51, product52, product53, product54, product55, product56, product57, product58, product59, product60]

    return render(request, 'schnoogle_a/winterB.html', {'products': products})

def nightwearB(request):
    product61 = Products() 
    product61.id = 74
    product61.name = 'Pink knit jumpsuit'
    product61.price = 2000
    image61 = 'static/images/winterset1.jpg'

    # Open the image file and create an ImageField object
    print(image61)
    with open(image61, 'rb') as f:
     product61.image.save('winterset1.jpg', File(f), save=True)

    product62 = Products() 
    product62.id = 75
    product62.name = 'Hooded jumpsuit'
    product62.price = 1560
    image62 = 'static/images/winterset2.jpg'

    # Open the image file and create an ImageField object
    print(image62)
    with open(image62, 'rb') as f:
     product62.image.save('winterset2.jpg', File(f), save=True)

    product63 = Products() 
    product63.id = 76
    product63.name = 'Cute bear jumpsuit'
    product63.price = 1460
    image63 = 'static/images/bs22.jpg'

    # Open the image file and create an ImageField object
    print(image63)
    with open(image63, 'rb') as f:
     product63.image.save('bs22.jpg', File(f), save=True)

    product64 = Products() 
    product64.id = 77
    product64.name = 'Brown woolen cap'
    product64.price = 1500
    image64 = 'static/images/wintercaps1.jpg'

    # Open the image file and create an ImageField object
    print(image64)
    with open(image64, 'rb') as f:
     product64.image.save('wintercaps1.jpg', File(f), save=True)

    product65 = Products() 
    product65.id = 78
    product65.name = 'Beanie Cap'
    product65.price = 450
    image65 = 'static/images/wintercaps2.jpg'

    # Open the image file and create an ImageField object
    print(image65)
    with open(image65, 'rb') as f:
     product65.image.save('wintercaps2.jpg', File(f), save=True)

    product66 = Products() 
    product66.id = 79
    product66.name = ' Grey cap and gloves set'
    product66.price = 390
    image66 = 'static/images/wintercaps3.jpg'

    # Open the image file and create an ImageField object
    print(image66)
    with open(image66, 'rb') as f:
     product66.image.save('wintercaps3.jpg', File(f), save=True)

    product67 = Products() 
    product67.id = 80
    product67.name = 'Sweatsuit'
    product67.price = 499
    image67 = 'static/images/winterset2.jpg'

    # Open the image file and create an ImageField object
    print(image67)
    with open(image67, 'rb') as f:
     product67.image.save('winterset2.jpg', File(f), save=True)

    product68 = Products() 
    product68.id = 81
    product68.name = 'Flannel Animal Jumpsuit'
    product68.price = 999
    image68 = 'static/images/winterset4.jpg'

    # Open the image file and create an ImageField object
    print(image68)
    with open(image68, 'rb') as f:
     product68.image.save('winterset4.jpg', File(f), save=True)

    product69 = Products() 
    product69.id = 82
    product69.name = 'Plaid duffle coat'
    product69.price = 1499
    image69 = 'static/images/winterset5.jpg'

    # Open the image file and create an ImageField object
    print(image69)
    with open(image69, 'rb') as f:
     product69.image.save('winterset5.jpg', File(f), save=True)

    product70 = Products() 
    product70.id = 83
    product70.name = 'Beige fur hoodie'
    product70.price = 899
    image70 = 'static/images/hood3.jpg'

    # Open the image file and create an ImageField object
    print(image70)
    with open(image70, 'rb') as f:
     product70.image.save('hood3.jpg', File(f), save=True)

    product71 = Products() 
    product71.id = 84
    product71.name = 'Black and grey fur hoodie'
    product71.price = 799
    image71 = 'static/images/hood2.jpg'

    # Open the image file and create an ImageField object
    print(image71)
    with open(image71, 'rb') as f:
     product71.image.save('hood2.jpg', File(f), save=True)

    product72 = Products() 
    product72.id = 85
    product72.name = 'Panda print hoodie'
    product72.price = 799
    image72 = 'static/images/hood1.jpg'

    # Open the image file and create an ImageField object
    print(image72)
    with open(image72, 'rb') as f:
     product72.image.save('hood1.jpg', File(f), save=True)

     products = [product61, product62, product63, product64, product65, product66, product67, product68, product69, product70, product71, product72]

    return render(request, 'schnoogle_a/nightwearB.html', {'products': products})

def casualwearG(request):
    product73 = Products() 
    product73.id = 86
    product73.name = 'Ribbed romper bodysuit'
    product73.price = 1220 
    image73 = 'static/images/TG1.jpg'

    # Open the image file and create an ImageField object
    print(image73)
    with open(image73, 'rb') as f:
     product73.image.save('TG1.jpg', File(f), save=True)

    product74 = Products() 
    product74.id = 87
    product74.name = 'Crochet dress'
    product74.price = 1160
    image74 = 'static/images/TG2.jpg'

    # Open the image file and create an ImageField object
    print(image74)
    with open(image74, 'rb') as f:
     product74.image.save('TG2.jpg', File(f), save=True)

    product75 = Products() 
    product75.id = 88
    product75.name = 'Cute babypink romper'
    product75.price = 1200
    image75 = 'static/images/TG3.jpg'

    # Open the image file and create an ImageField object
    print(image75)
    with open(image75, 'rb') as f:
     product75.image.save('TG3.jpg', File(f), save=True)

    product76 = Products() 
    product76.id = 89
    product76.name = 'Classic french frock'
    product76.price = 800
    image76 = 'static/images/TG4.jpg'

    # Open the image file and create an ImageField object
    print(image76)
    with open(image76, 'rb') as f:
     product76.image.save('TG4.jpg', File(f), save=True)

    product77 = Products() 
    product77.id = 90
    product77.name = 'Floral print frock'
    product77.price = 850
    image77 = 'static/images/TG5.jpg'

    # Open the image file and create an ImageField object
    print(image77)
    with open(image77, 'rb') as f:
     product77.image.save('TG5.jpg', File(f), save=True)

    product78 = Products() 
    product78.id = 91
    product78.name = 'Yarn pattern frock'
    product78.price = 1390
    image78 = 'static/images/TG6.jpg'

    # Open the image file and create an ImageField object
    print(image78)
    with open(image78, 'rb') as f:
     product78.image.save('TG6.jpg', File(f), save=True)

    product79 = Products() 
    product79.id = 92
    product79.name = 'Stylish off shoulder top'
    product79.price = 599
    image79 = 'static/images/TG7.jpg'

    # Open the image file and create an ImageField object
    print(image79)
    with open(image79, 'rb') as f:
     product79.image.save('TG7.jpg', File(f), save=True)

    product80 = Products() 
    product80.id = 93
    product80.name = 'Floral crop top'
    product80.price = 799
    image80 = 'static/images/TG8.jpg'

    # Open the image file and create an ImageField object
    print(image80)
    with open(image80, 'rb') as f:
     product80.image.save('TG8.jpg', File(f), save=True)

    product81 = Products() 
    product81.id = 94
    product81.name = 'Plaid jacket & Dress set'
    product81.price = 2499
    image81 = 'static/images/TG9.jpg'

    # Open the image file and create an ImageField object
    print(image81)
    with open(image81, 'rb') as f:
     product81.image.save('TG9.jpg', File(f), save=True)

    product82 = Products() 
    product82.id = 95
    product82.name = 'Solid Cami Top & Print Blazer & Skirt'
    product82.price = 1299
    image82 = 'static/images/TG12.jpg'

    # Open the image file and create an ImageField object
    print(image82)
    with open(image82, 'rb') as f:
     product82.image.save('TG12.jpg', File(f), save=True)

    product83 = Products() 
    product83.id = 96
    product83.name = 'Bust Cami Top & Blouse & Shorts'
    product83.price = 899
    image83 = 'static/images/TG11.jpg'

    # Open the image file and create an ImageField object
    print(image83)
    with open(image83, 'rb') as f:
     product83.image.save('TG11.jpg', File(f), save=True)

    product84 = Products() 
    product84.id = 97
    product84.name = 'Ruffle Trim Top & Bow Décor Shorts'
    product84.price = 999
    image84 = 'static/images/TG10.jpg'

    # Open the image file and create an ImageField object
    print(image84)
    with open(image84, 'rb') as f:
     product84.image.save('TG10.jpg', File(f), save=True)

     products = [product73, product74, product75, product76, product77, product78, product79, product80, product81, product82, product83, product84]

    return render(request, 'schnoogle_a/casualwearG.html', {'products': products})

def weddingwearG(request):
    product85 = Products() 
    product85.id = 98
    product85.name = 'White floral frock '
    product85.price = 1300 
    image85 = 'static/images/wg1.jpg'

    # Open the image file and create an ImageField object
    print(image85)
    with open(image85, 'rb') as f:
     product85.image.save('wg1.jpg', File(f), save=True)

    product86 = Products() 
    product86.id = 99
    product86.name = 'Pink frock with beautiful lace'
    product86.price = 1160
    image86 = 'static/images/wg2.jpg'

    # Open the image file and create an ImageField object
    print(image86)
    with open(image86, 'rb') as f:
     product86.image.save('wg2.jpg', File(f), save=True)

    product87 = Products() 
    product87.id = 100
    product87.name = 'Beautiful princess dress'
    product87.price = 1999
    image87 = 'static/images/wwg3.jpg'

    # Open the image file and create an ImageField object
    print(image87)
    with open(image87, 'rb') as f:
     product87.image.save('wwg3.jpg', File(f), save=True)

    product88 = Products() 
    product88.id = 101
    product88.name = 'Garara set'
    product88.price = 1999
    image88 = 'static/images/wg4.jpg'

    # Open the image file and create an ImageField object
    print(image88)
    with open(image88, 'rb') as f:
     product88.image.save('wg4.jpg', File(f), save=True)

    product89 = Products() 
    product89.id = 102
    product89.name = 'Yellow suit'
    product89.price = 850
    image89 = 'static/images/wg5.jpg'

    # Open the image file and create an ImageField object
    print(image89)
    with open(image89, 'rb') as f:
     product89.image.save('wg5.jpg', File(f), save=True)

    product90 = Products() 
    product90.id = 103
    product90.name = 'Yellow kurta'
    product90.price = 490
    image90 = 'static/images/wg6.jpg'

    # Open the image file and create an ImageField object
    print(image90)
    with open(image90, 'rb') as f:
     product90.image.save('wg6.jpg', File(f), save=True)

    product91 = Products() 
    product91.id = 104
    product91.name = 'Sequin frock'
    product91.price = 999
    image91 = 'static/images/wed1g.jpg'

    # Open the image file and create an ImageField object
    print(image91)
    with open(image91, 'rb') as f:
     product91.image.save('wed1g.jpg', File(f), save=True)

    product92 = Products() 
    product92.id = 105
    product92.name = 'White sharara set'
    product92.price = 2599
    image92 = 'static/images/wed2g.jpg'

    # Open the image file and create an ImageField object
    print(image92)
    with open(image92, 'rb') as f:
     product92.image.save('wed2g.jpg', File(f), save=True)

    product93 = Products() 
    product93.id = 106
    product93.name = 'Peacock blue Anarkali set'
    product93.price = 2499
    image93 = 'static/images/wed3g.jpg'

    # Open the image file and create an ImageField object
    print(image93)
    with open(image93, 'rb') as f:
     product93.image.save('wed3g.jpg', File(f), save=True)

    product94 = Products() 
    product94.id = 107
    product94.name = 'Pastel green sharara set'
    product94.price = 3299
    image94 = 'static/images/wed4g.jpg'

    # Open the image file and create an ImageField object
    print(image94)
    with open(image94, 'rb') as f:
     product94.image.save('wed4g.jpg', File(f), save=True)

    product95 = Products() 
    product95.id = 108
    product95.name = 'Pink salwar suit'
    product95.price = 1999
    image95 = 'static/images/wed5g.jpg'

    # Open the image file and create an ImageField object
    print(image95)
    with open(image95, 'rb') as f:
     product95.image.save('wed5g.jpg', File(f), save=True)

    product96 = Products() 
    product96.id = 109
    product96.name = 'Saree'
    product96.price = 3999
    image96 = 'static/images/wed6g.jpg'

    # Open the image file and create an ImageField object
    print(image96)
    with open(image96, 'rb') as f:
     product96.image.save('wed6g.jpg', File(f), save=True)

     products = [product85, product86, product87, product88, product89, product90, product91, product92, product93, product94, product95, product96]

    return render(request, 'schnoogle_a/weddingwearG.html', {'products': products})

def partyB(request):
    product97 = Products() 
    product97.id = 110
    product97.name = 'Toddler grey suit '
    product97.price = 1900 
    image97 = 'static/images/wb2.jpg'

    # Open the image file and create an ImageField object
    print(image97)
    with open(image97, 'rb') as f:
     product97.image.save('wb2.jpg', File(f), save=True)

    product98 = Products() 
    product98.id = 111
    product98.name = 'Waistcoat style suit'
    product98.price = 3000
    image98 = 'static/images/wb3.jpg'

    # Open the image file and create an ImageField object
    print(image98)
    with open(image98, 'rb') as f:
     product98.image.save('wb3.jpg', File(f), save=True)

    product99 = Products() 
    product99.id = 112
    product99.name = 'Velvet suit'
    product99.price = 4000
    image99 = 'static/images/wb6.jpg'

    # Open the image file and create an ImageField object
    print(image99)
    with open(image99, 'rb') as f:
     product99.image.save('wb6.jpg', File(f), save=True)

    product100 = Products() 
    product100.id = 113
    product100.name = 'Light blue jumpsuit'
    product100.price = 1000
    image100 = 'static/images/wb1.jpg'

    # Open the image file and create an ImageField object
    print(image100)
    with open(image100, 'rb') as f:
     product100.image.save('wb1.jpg', File(f), save=True)

    product101 = Products() 
    product101.id = 114
    product101.name = 'Cotton romper'
    product101.price = 1850
    image101 = 'static/images/wb4.jpg'

    # Open the image file and create an ImageField object
    print(image101)
    with open(image101, 'rb') as f:
     product101.image.save('wb4.jpg', File(f), save=True)

    product102 = Products() 
    product102.id = 115
    product102.name = 'Silk romper'
    product102.price = 1390
    image102 = 'static/images/wb5.jpg'

    # Open the image file and create an ImageField object
    print(image102)
    with open(image102, 'rb') as f:
     product102.image.save('wg5.jpg', File(f), save=True)

    product103 = Products() 
    product103.id = 116
    product103.name = 'White cotton kurta'
    product103.price = 999
    image103 = 'static/images/ib.jpg'

    # Open the image file and create an ImageField object
    print(image103)
    with open(image103, 'rb') as f:
     product103.image.save('ib.jpg', File(f), save=True)

    product104 = Products() 
    product104.id = 117
    product104.name = 'Dhoti kurta'
    product104.price = 1299
    image104 = 'static/images/ib2.jpg'

    # Open the image file and create an ImageField object
    print(image104)
    with open(image104, 'rb') as f:
     product104.image.save('ib2.jpg', File(f), save=True)

    product105 = Products() 
    product105.id = 118
    product105.name = 'Paithani jacket'
    product105.price = 3199
    image105 = 'static/images/ib3.jpg'

    # Open the image file and create an ImageField object
    print(image105)
    with open(image105, 'rb') as f:
     product105.image.save('ib3.jpg', File(f), save=True)

    product106 = Products() 
    product106.id = 119
    product106.name = 'Classic Style Fashion Suit Set'
    product106.price = 3999
    image106 = 'static/images/ib4.jpg'

    # Open the image file and create an ImageField object
    print(image106)
    with open(image106, 'rb') as f:
     product106.image.save('ib4.jpg', File(f), save=True)

    product107 = Products() 
    product107.id = 120
    product107.name = 'Dark Blue blazer and bow tie set'
    product107.price = 2599
    image107 = 'static/images/sale2.jpg'

    # Open the image file and create an ImageField object
    print(image107)
    with open(image107, 'rb') as f:
     product107.image.save('sale2.jpg', File(f), save=True)

    product108 = Products() 
    product108.id = 121
    product108.name = 'Dolce & Gabbana Jacquard Blazer'
    product108.price = 8999
    image108 = 'static/images/ib5.jpg'

    # Open the image file and create an ImageField object
    print(image108)
    with open(image108, 'rb') as f:
     product108.image.save('ib5.jpg', File(f), save=True)

     products = [product97, product98, product99, product100, product101, product102, product103, product104, product105, product106, product107, product108]

    return render(request, 'schnoogle_a/partyB.html', {'products': products})

def footwearG(request):
    product109 = Products() 
    product109.id = 123
    product109.name = 'Sports shoes'
    product109.price = 1160 
    image109 = 'static/images/sg2.jpg'

    # Open the image file and create an ImageField object
    print(image109)
    with open(image109, 'rb') as f:
     product109.image.save('sg2.jpg', File(f), save=True)

    product110 = Products() 
    product110.id = 124
    product110.name = 'Winter shoes'
    product110.price = 400
    image110 = 'static/images/sg3.jpg'

    # Open the image file and create an ImageField object
    print(image110)
    with open(image110, 'rb') as f:
     product110.image.save('sg3.jpg', File(f), save=True)

    product111 = Products() 
    product111.id = 125
    product111.name = 'Plaid woven sandal'
    product111.price = 400
    image111 = 'static/images/sg4.jpg'

    # Open the image file and create an ImageField object
    print(image111)
    with open(image111, 'rb') as f:
     product111.image.save('sg4.jpg', File(f), save=True)

    product112 = Products() 
    product112.id = 126
    product112.name = 'Bow applique sandal'
    product112.price = 850
    image112 = 'static/images/sg5.jpg'

    # Open the image file and create an ImageField object
    print(image112)
    with open(image112, 'rb') as f:
     product112.image.save('sg5.jpg', File(f), save=True)

    product113 = Products() 
    product113.id = 127
    product113.name = 'Floral flats'
    product113.price = 390
    image113 = 'static/images/sg6.jpg'

    # Open the image file and create an ImageField object
    print(image113)
    with open(image113, 'rb') as f:
     product113.image.save('sg6.jpg', File(f), save=True)

    product114 = Products() 
    product114.id = 128
    product114.name = 'Cute baby booties'
    product114.price = 399
    image114 = 'static/images/sg7.jpg'

    # Open the image file and create an ImageField object
    print(image114)
    with open(image114, 'rb') as f:
     product114.image.save('sg7.jpg', File(f), save=True)

    product115 = Products() 
    product115.id = 129
    product115.name = 'Bow fluffy socks'
    product115.price = 499
    image115 = 'static/images/sg8.jpg'

    # Open the image file and create an ImageField object
    print(image115)
    with open(image115, 'rb') as f:
     product115.image.save('sg8.jpg', File(f), save=True)

    product116 = Products() 
    product116.id = 130
    product116.name = 'Knee length socks'
    product116.price = 499
    image116 = 'static/images/sg9.jpg'

    # Open the image file and create an ImageField object
    print(image116)
    with open(image116, 'rb') as f:
     product116.image.save('sg9.jpg', File(f), save=True)

    product117 = Products() 
    product117.id = 122
    product117.name = 'Leather shoes'
    product117.price = 400
    image117 = 'static/images/sg1.jpg'

    # Open the image file and create an ImageField object
    print(image117)
    with open(image117, 'rb') as f:
     product117.image.save('sg1.jpg', File(f), save=True)

    product118 = Products() 
    product118.id = 131
    product118.name = 'Bowtie ballerina shoes'
    product118.price = 699
    image118 = 'static/images/sg10.jpg'

    # Open the image file and create an ImageField object
    print(image118)
    with open(image118, 'rb') as f:
     product118.image.save('sg10.jpg', File(f), save=True)

    product119 = Products() 
    product119.id = 132
    product119.name = 'Beige bowtie ballerina shoes'
    product119.price = 799
    image119 = 'static/images/sg11.jpg'

    # Open the image file and create an ImageField object
    print(image119)
    with open(image119, 'rb') as f:
     product119.image.save('sg11.jpg', File(f), save=True)

    product120 = Products() 
    product120.id = 133
    product120.name = 'Lace-up pink boots'
    product120.price = 1299
    image120 = 'static/images/sg12.jpg'

    # Open the image file and create an ImageField object
    print(image120)
    with open(image120, 'rb') as f:
     product120.image.save('sg12.jpg', File(f), save=True)

     products = [product109, product110, product111, product112, product113, product114, product115, product116, product117, product118, product119, product120]

    return render(request, 'schnoogle_a/footwearG.html', {'products': products})

    
def winterG(request):
    product121 = Products() 
    product121.id = 134
    product121.name = 'Brown woolen jacket'
    product121.price = 1600 
    image121 = 'static/images/wwg.jpg'

    # Open the image file and create an ImageField object
    print(image121)
    with open(image121, 'rb') as f:
     product121.image.save('wwg.jpg', File(f), save=True)

    product122 = Products() 
    product122.id = 135
    product122.name = 'Puffer jacket'
    product122.price = 1160
    image122 = 'static/images/wwg2.jpg'

    # Open the image file and create an ImageField object
    print(image122)
    with open(image122, 'rb') as f:
     product122.image.save('wwg2.jpg', File(f), save=True)

    product123 = Products() 
    product123.id = 136
    product123.name = 'Winter frock'
    product123.price = 1000
    image123 = 'static/images/wwg3.jpg'

    # Open the image file and create an ImageField object
    print(image123)
    with open(image123, 'rb') as f:
     product123.image.save('wwg3.jpg', File(f), save=True)

    product124 = Products() 
    product124.id = 137
    product124.name = 'Furry jacket'
    product124.price = 1400
    image124 = 'static/images/wwg4.jpg'

    # Open the image file and create an ImageField object
    print(image124)
    with open(image124, 'rb') as f:
     product124.image.save('wwg4.jpg', File(f), save=True)

    product125 = Products() 
    product125.id = 138
    product125.name = 'Sweatshirt'
    product125.price = 1850
    image125 = 'static/images/wwg5.jpg'

    # Open the image file and create an ImageField object
    print(image125)
    with open(image125, 'rb') as f:
     product125.image.save('wwg5.jpg', File(f), save=True)

    product126 = Products() 
    product126.id = 139
    product126.name = 'Coat'
    product126.price = 1390
    image126 = 'static/images/wwg6.jpg'

    # Open the image file and create an ImageField object
    print(image126)
    with open(image126, 'rb') as f:
     product126.image.save('wwg6.jpg', File(f), save=True)

    product127 = Products() 
    product127.id = 140
    product127.name = 'Cable-Knit cap'
    product127.price = 599
    image127 = 'static/images/wwg7.jpg'

    # Open the image file and create an ImageField object
    print(image127)
    with open(image127, 'rb') as f:
     product127.image.save('wwg7.jpg', File(f), save=True)

    product128 = Products() 
    product128.id = 141
    product128.name = 'Cute bear ears cap and gloves'
    product128.price = 499
    image128 = 'static/images/ww8.jpg'

    # Open the image file and create an ImageField object
    print(image128)
    with open(image128, 'rb') as f:
     product128.image.save('ww8.jpg', File(f), save=True)

    product129 = Products() 
    product129.id = 142
    product129.name = 'Fleece trapper cap'
    product129.price = 400
    image129 = 'static/images/wwg9.jpg'

    # Open the image file and create an ImageField object
    print(image129)
    with open(image129, 'rb') as f:
     product129.image.save('wwg9.jpg', File(f), save=True)

    product130 = Products() 
    product130.id = 143
    product130.name = 'Slant Pocket Fuzzy Trim Hooded Down Coat'
    product130.price = 5999
    image130 = 'static/images/ww3.jpg'

    # Open the image file and create an ImageField object
    print(image130)
    with open(image130, 'rb') as f:
     product130.image.save('ww3.jpg', File(f), save=True)

    product131 = Products() 
    product131.id = 144
    product131.name = 'Yellow Fuzzy Trim Down Coat With Gloves'
    product131.price = 7999
    image131 = 'static/images/ww4.jpg'

    # Open the image file and create an ImageField object
    print(image131)
    with open(image131, 'rb') as f:
     product131.image.save('ww4.jpg', File(f), save=True)

    product132 = Products() 
    product132.id = 145
    product132.name = 'Open Front Fuzzy Vest Coat'
    product132.price = 3999
    image132 = 'static/images/ww5.jpg'

    # Open the image file and create an ImageField object
    print(image132)
    with open(image132, 'rb') as f:
     product132.image.save('ww5.jpg', File(f), save=True)

     products = [product121, product122, product123, product124, product125, product126, product127, product128, product129, product130, product131, product132]

    return render(request, 'schnoogle_a/winterG.html', {'products': products})

def nightwearG(request):
    product133 = Products() 
    product133.id = 146
    product133.name =  'Cotton rompers'
    product133.price = 600 
    image133 = 'static/images/nwg.jpg'

    # Open the image file and create an ImageField object
    print(image133)
    with open(image133, 'rb') as f:
     product133.image.save('nwg.jpg', File(f), save=True)

    product134 = Products() 
    product134.id = 147
    product134.name = 'Cotton sleepsuit'
    product134.price = 760
    image134 = 'static/images/nwg2.jpg'

    # Open the image file and create an ImageField object
    print(image134)
    with open(image134, 'rb') as f:
     product134.image.save('nwg2.jpg', File(f), save=True)

    product135 = Products() 
    product135.id = 148
    product135.name = 'Babypink top & pyjama set'
    product135.price = 700
    image135 = 'static/images/nwg3.jpg'

    # Open the image file and create an ImageField object
    print(image135)
    with open(image135, 'rb') as f:
     product135.image.save('nwg3.jpg', File(f), save=True)

    product136 = Products() 
    product136.id = 149
    product136.name = 'Tshirt and shorts set'
    product136.price = 900
    image136 = 'static/images/nwg4.jpg'

    # Open the image file and create an ImageField object
    print(image136)
    with open(image136, 'rb') as f:
     product136.image.save('nwg4.jpg', File(f), save=True)

    product137 = Products() 
    product137.id = 150
    product137.name = 'White gown'
    product137.price = 850
    image137 = 'static/images/nwg5.jpg'

    # Open the image file and create an ImageField object
    print(image137)
    with open(image137, 'rb') as f:
     product137.image.save('nwg5.jpg', File(f), save=True)

    product138 = Products() 
    product138.id = 151
    product138.name = 'Multicolor suit'
    product138.price = 1200
    image138 = 'static/images/nwg6.jpg'

    # Open the image file and create an ImageField object
    print(image138)
    with open(image138, 'rb') as f:
     product138.image.save('nwg6.jpg', File(f), save=True)

    product139 = Products() 
    product139.id = 152
    product139.name = 'Multicolor suit'
    product139.price = 1199
    image139 = 'static/images/nwg7.jpg'

    # Open the image file and create an ImageField object
    print(image139)
    with open(image139, 'rb') as f:
     product139.image.save('nwg7.jpg', File(f), save=True)

    product140 = Products() 
    product140.id = 153
    product140.name = 'Full sleeves nightwear'
    product140.price = 1129
    image140 = 'static/images/nwg8.jpg'

    # Open the image file and create an ImageField object
    print(image140)
    with open(image140, 'rb') as f:
     product140.image.save('nwg8.jpg', File(f), save=True)

    product141 = Products() 
    product141.id = 154
    product141.name = 'Full sleeves nightwear'
    product141.price = 499
    image141 = 'static/images/nwg9.jpg'

    # Open the image file and create an ImageField object
    print(image141)
    with open(image141, 'rb') as f:
     product141.image.save('nwg9.jpg', File(f), save=True)

    product142 = Products() 
    product142.id = 155
    product142.name = 'Graphic Top'
    product142.price = 399
    image142 = 'static/images/nwg10.jpg'

    # Open the image file and create an ImageField object
    print(image142)
    with open(image142, 'rb') as f:
     product142.image.save('nwg10.jpg', File(f), save=True)

    product143 = Products() 
    product143.id = 156
    product143.name = 'Multicolor striped t-shirt and bottom set'
    product143.price = 499
    image143 = 'static/images/nwg11.jpg'

    # Open the image file and create an ImageField object
    print(image143)
    with open(image143, 'rb') as f:
     product143.image.save('nwg11.jpg', File(f), save=True)

    product144 = Products() 
    product144.id = 157
    product144.name = 'Baby pink night wear'
    product144.price = 500 
    image144 = 'static/images/nwg12.jpg'

    # Open the image file and create an ImageField object
    print(image144)
    with open(image144, 'rb') as f:
     product144.image.save('nwg12.jpg', File(f), save=True)

     products = [product133, product134, product135, product136, product137, product138, product139, product140, product141, product142, product143, product144]

    return render(request, 'schnoogle_a/nightwearG.html', {'products': products})


def parenting(request):
    return render(request, 'schnoogle_a/parenting.html')

def signUp(request):
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            for error in form.errors:
                messages.warning(request, f"{error}: {form.errors[error][0]}")
            return redirect('signup')
    else:
        form = CreateUserForm()
        return render(request, 'schnoogle_a/signup.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        contact=Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message',)
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.message=message
        contact.save()
       
        return HttpResponse("<h1>THANK YOU FOR CONTACTING US</h1>")
    
    return render(request, 'schnoogle_a/contact.html')

    