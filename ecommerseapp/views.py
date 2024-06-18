from django.shortcuts import render , redirect, HttpResponse, get_object_or_404
from .models import Contact , Product, CartItem , Order
from django.contrib import messages
from math import ceil
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
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
            user = request.user,
            product = product
        )
        cart_item.quantity += quantity
        cart_item.save()
        return redirect('cart')



@login_required(login_url="/")
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    item_list = []
    for cart_item in cart_items:
        product = cart_item.product
        quantity = cart_item.quantity
        user = cart_item.user
        image = Product.objects.get(product_name=product).image
        id = cart_item.id
        price = Product.objects.get(product_name=product).price
        item_dict = {
            "user" : user,
            "name" : product,
            "quantity" : quantity,
            "image":image,
            "id" : id,
            "price" : price*quantity,
        } 
        item_list.append(item_dict)
    # print(item_list)
    return render(request, 'cart.html', {'cart_items': item_list})


def remove_cart_item(request,id):
    # id = request.data.get('id')
    if request.method == "POST":
        cart_item = get_object_or_404(CartItem, id=id)
        cart_item.delete()
    return redirect(view_cart)


def checkout(request,id):
    print("iiiiiiiiiiidddddddddddddddddddddddd",id)
    form = OrderForm
    product = Product.objects.get(id=id)
    print(product.price)
    if request.method == "POST":
        
        return render("Thank you for shopping...........?")
    return render(request,"checkout.html",{"form": form,"product":product})