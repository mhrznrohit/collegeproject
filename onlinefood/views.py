from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import CartItems, Item
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.db.models import Sum

# Create your views here.

def index(request):
    data=Item.objects.all()
    if request.method=='POST':
        # citems=CartItems.objects.get(id=itemid)
        itemid=int(request.POST['item-id'])
        itemtitle=request.POST['item-title']
        citems=CartItems(userid=request.user,item=Item.objects.get(id=itemid),itemtitle=itemtitle)
        citems.save()
    return render(request, 'index.html',{'data':data})


# def login(request):
#     return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
         form = UserRegistrationForm(request.POST)
         if form.is_valid():
             form.save()
             user = form.cleaned_data.get('username')
             messages.success(request, 'Account was created for ' + user)
             return redirect('login')
    else:
        form=UserRegistrationForm()

    context = {'form':form}
    
    return render(request, 'register.html',context)
    
def user_login(request):
    
    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        user_data = authenticate(username=username, password=password)
        if user_data is  None:
            messages.error(request,'Incorrect Username or Password');
        if user_data is not None:
            data=Item.objects.all()

            login(request, user_data)
            uname=user_data.get_username
            messages.success(request,'Logged in Sucessfully');
            return redirect('index')
            

    if request.user.is_authenticated==True:
        return redirect('index')
        
    else:
        return render(request, 'login.html')   

def cart(request):
    if request.user.is_authenticated==True:
        uid=request.user.id
        get_items=CartItems.objects.filter(userid=uid,status='Active')
        deliver_item=CartItems.objects.filter(userid=uid,status='Delivered').order_by('-id')[:5]
        bill = get_items.aggregate(Sum('item__price'))
        sum = bill.get("item__price__sum")


        if request.method=='POST':
            itemid=request.POST['item-id']
            CartItems.objects.filter(id=itemid).delete()


        return render(request,'cart.html',{'item':get_items,'delivery':deliver_item, 'total':sum})
        
    else:
       return redirect('login')

    return render(request,'cart.html')


@login_required
def logout_user(request):
    if User.is_authenticated:
        logout(request)
        messages.error(request,'Logout in Sucessfully');
        return redirect('index')        


@login_required
def checkout(request):
    get_items=CartItems.objects.filter(userid=request.user,status='Active')
    bill = get_items.aggregate(Sum('item__price'))
    sum = bill.get("item__price__sum")
    if request.method=='POST':
        
        amt=request.POST['pay_amt']
        location_info=request.POST['CartItems-location']
        # if sum==amt:
        #     print('12')
        update=CartItems.objects.filter(userid=request.user,status='Active').update(status='Delivered',location=location_info)
        
    return render(request, 'checkout.html',{'item':get_items,'total':sum})



