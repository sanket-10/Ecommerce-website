from django.shortcuts import render , redirect
from .models import Contact , Product
from django.contrib import messages
from math import ceil
# Create your views here.


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

def about(request):
    return render(request,'about.html')

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"please login and try again.")
        return redirect('/auth/login')
    currentuser = request.user.username

    return render(request,'profile.html')
