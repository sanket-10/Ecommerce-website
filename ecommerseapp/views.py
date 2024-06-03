from django.shortcuts import render , redirect
from .models import Contact , Product, CartItem
from django.contrib import messages
from math import ceil
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="/")
def index(request):
    allprods = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nSlides),nSlides])

    params = {'allprods': allprods}
    return render(request,'index.html',params)


@login_required(login_url="/")
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        pnumber = request.POST['pnumber']
        myquery = Contact(name=name,email=email,desc=desc,phonenumber=pnumber)
        myquery.save()
        messages.info(request,"We will get back to you soon.")
        return render(request, 'contact.html')
    return render(request,'contact.html')

@login_required(login_url="/")
def about(request):
    return render(request,'about.html')



@login_required(login_url="/")
def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"please login and try again.")
        return redirect('/auth/login')
    currentuser_name = request.user.username
    # print(currentuser_name,"-------------------------------")
    user_details = User.objects.get(username=currentuser_name)
    # print(user_details)

    return render(request,'profile.html',{"user":user_details})




@login_required(login_url="/")
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        # assuming you have a form with quantity input
        quantity = int(request.POST.get('quantity', 1))
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product
        )
        cart_item.quantity += quantity
        cart_item.save()
        return redirect('cart')



@login_required(login_url="/")
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    print(request)
    item_list = []
    for item in cart_items:
        print(item.pk)
        cart_products = Product.objects.get(id=item.pk)
        item_list.append(cart_products)
    print(item_list)
    return render(request, 'cart.html', {'cart_items': item_list})