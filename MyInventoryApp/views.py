from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Supplier, WaterBottle, Account
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def view_supplier(request):
    user_id = request.session.get('user.id')
    user = get_object_or_404(Account, pk=user_id) if user_id else None

    supplier_objects = Supplier.objects.all()
    return render(request, 'myapp/view_supplier.html', {'supplier':supplier_objects, 'user': user})

def view_bottles(request):
    bottle_objects = WaterBottle.objects.all()
    return render(request, 'myapp/view_bottles.html', {'waterBottle':bottle_objects})

def add_bottle(request):
    if request.method == "POST":
        sku = request.POST.get('sku')
        brand = request.POST.get('brand')
        cost = request.POST.get('cost')
        size = request.POST.get('size')
        mouthSize = request.POST.get('mouthSize')
        color = request.POST.get('color')
        suppliedBy_id = request.POST.get('suppliedBy')
        currentQuantity = request.POST.get('currentQuantity')
        
        suppliedBy = Supplier.objects.get(id=suppliedBy_id)
        WaterBottle.objects.create(sku=sku, brand=brand, cost=cost, size=size, mouthSize=mouthSize, color=color, suppliedBy=suppliedBy, currentQuantity=currentQuantity)
        return redirect('view_bottles')
    
    suppliers = Supplier.objects.all()
    return render(request, 'myapp/add_bottle.html', {'suppliedBy': suppliers})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        
        try:
            account = Account.objects.get(username=username)
            if check_password(password1, account.password1):
                request.session['user.id'] = account.pk
                return redirect('view_supplier')
            else:
                messages.error(request, "Invalid login. Username does not match Password.")
        except Account.DoesNotExist:
            messages.error(request, "Invalid login. Account does not exist.")
    
    return render(request, 'myapp/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if Account.objects.filter(username=username).exists():
            messages.error(request, "Account already exists.")
        elif password1 != password2:
            messages.error(request, "Passwords do not match.")
        else:
            hashed_pw = make_password(password1)
            Account.objects.create(username=username, password1=hashed_pw)
            messages.success(request, "Account created successfully.")
            return redirect('login')
    
    return render(request, 'myapp/signup.html')

def view_bottle_details(request, pk):
    b = get_object_or_404(WaterBottle, pk=pk)
    s = Supplier.objects.all()
    return render(request, 'myapp/view_bottle_details.html', {'b':b, 's':s})

def delete_bottle(request, pk):
    WaterBottle.objects.filter(pk=pk).delete()
    return redirect('view_bottles')

def manage_account(request, pk):
   user = get_object_or_404(Account, pk=pk)
   return render(request, 'myapp/manage_account.html', {'user':user})

def change_password(request, pk):
    user_id = request.session.get('user.id')
    if not user_id or int(pk) != user_id:
        return redirect("login")
    
    user=get_object_or_404(Account, pk=user_id)

    if request.method == "POST":
        current_password =  request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not check_password(current_password, user.password1):
            messages.error(request, "Incorrect current password.")
            return redirect("change_password", pk=pk)

        if new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return redirect("change_password", pk=pk)

        user.password1 = make_password(new_password)
        user.save()
        messages.success(request, "Password changed successfully!")
        return redirect("manage_account", pk=pk)

    return render(request, "myapp/change_password.html", {'user': user})

def delete_account(request, pk):
    user = get_object_or_404(Account, pk=pk)
    user.delete()
    messages.success(request, "Account deleted successfully")
    return redirect('login')

def logout(request):
    request.session.flush()
    return redirect("login")