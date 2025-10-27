from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View

# Create your views here.
from .forms import ProductForm, RegisterForm
from .models import Product


# Home view
# def home_view(request):
#     return render(request, 'invApp/home.html')

# CRUD

# Create View


def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})


# Read View
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'product': products})


# Update View
def produdct_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})


# Delete View
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html', {'poduct': product})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if username is not None and password is not None:
                user = User.objects.create_user(
                    username=username, password=password)
                login(request, user)
                return redirect('home')
        else:
            form.add_error(None, "Username and Password required!")
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get(
                'next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
        return render(request, 'accounts/login.html', {'error': error_message})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('home')


@login_required
def home_view(request):
    return render(request, 'invApp/home.html')


class ProtectedView(LoginRequiredMixin, View):
    login_url = 'login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'invApp/home.html')
